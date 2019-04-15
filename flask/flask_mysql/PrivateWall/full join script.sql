select * from messages;

select * from users;


select messages.id as 'ID of message itself', messages.sender_id AS 'Message Sender ID', receiver_id AS 'Message Receiver ID', message_content, users.fname AS 'Sender fname' , users.lname AS 'Sender lname', users.email AS 'Sender email' , users.pw_hash AS 'Sender hashed pw', user_as_message_receiver.fname AS 'Message Receiver first name', user_as_message_receiver.lname AS 'Message Receiver Last Name', user_as_message_receiver.email AS 'Message Receiver email', user_as_message_receiver.pw_hash AS 'Receiver hashed pw'
from messages
JOIN users on messages.sender_id =users.id
JOIN users AS user_as_message_receiver ON messages.receiver_id = user_as_message_receiver.id







;

