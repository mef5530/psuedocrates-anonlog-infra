### /api/register
- @param username
- @param password

### /api/login
- @param username
- @param password

### /api/store_user_data
- @param data
- @param username
- @param name
- @param bio

### /api/get_user_data SKIP

### /api/chatbot/initialize
- @param user_bio
- @param selected_scenario
- @param username
- @param chatbot_id

### /api/chatbot/send
- @param chatbot_id
- @param message
- @param response

### /api/ethics-engine/send
- @param chatbot_id
- @param background
- @param dilemma
- @param options
- @param desired_result
- @param response


"message": "<NAMED ENTITY 4: username>: <message_from_user> Hi my name is <NAMED ENTITY 2: PERSON> my phone number is 
1 <NAMED ENTITY 13: PHONE_NUMBER> my social security is <NAMED ENTITY 12: DATE_TIME> my ip is <NAMED ENTITY 11: IP_ADDRESS> I live in <NAMED ENTITY 10: LOCATION>, <NAMED ENTITY 9: LOCATION> </message_from_user>