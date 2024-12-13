from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine
from sqlalchemy import or_, and_
import datetime

from anonalog_server.model import Session
from anonalog_server.model.schema import NamedEntityMapping

analyzer = AnalyzerEngine()
anonymizer = AnonymizerEngine()

def pseudonymize_named_entity(chatbot_id, named_str, entity_type):
    if not chatbot_id:
        chatbot_id = 'none'
    
    name = named_str.lower()

    with Session() as session:
        existing_map = session.query(NamedEntityMapping).filter(and_(or_(NamedEntityMapping.chatbot_id == chatbot_id, NamedEntityMapping.chatbot_id == 'none'), NamedEntityMapping.name == name)).first()
        if existing_map:
            return existing_map.pseudonym
        else:
            count = session.query(NamedEntityMapping).filter(or_(NamedEntityMapping.chatbot_id == chatbot_id, NamedEntityMapping.chatbot_id == 'none')).count()
            pseudonym = f'<NAMED ENTITY {count+1}: {entity_type}>'
            new_map = NamedEntityMapping(chatbot_id=chatbot_id, name=name, pseudonym=pseudonym)
            session.add(new_map)
            session.commit()
            return pseudonym

def anonymize_data_field(chatbot_id=None, **kwargs):
    print(f'start: {datetime.datetime.utcnow()}')
    result = {}

    for field, value in kwargs.items():
        if not value:
            result[field] = value
            continue

        if field in ['username', 'name']:
            pseudonym = pseudonymize_named_entity(
                chatbot_id=chatbot_id,
                named_str=value.strip(),
                entity_type=field
            )
            result[field] = pseudonym
            continue

        if field == 'password':
            result[field] = '<PASSWORD>'
            continue

        tokens = analyzer.analyze(text=value, entities=[], language='en', score_threshold=0.25)
        if tokens:
            tokens_sorted = sorted(tokens, key=lambda x: x.start, reverse=True)
            anonymized_text = value
            for tok in tokens_sorted:
                print(tok)
                entity_str = value[tok.start:tok.end]
                pseudonym = pseudonymize_named_entity(
                    chatbot_id=chatbot_id,
                    named_str=entity_str,
                    entity_type=tok.entity_type
                )
                anonymized_text = anonymized_text[:tok.start] + pseudonym + anonymized_text[tok.end:]
            result[field] = anonymized_text
        else:
            result[field] = value
    print(f'end: {datetime.datetime.utcnow()}')
    return result