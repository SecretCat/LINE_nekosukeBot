def type ():
    13:"TO_BE_INVITED_GROUP"#招待される
    16:"JOIN_GROUP"#グループに参加する
    17:"OTHER_PEOPLE_JOIN"#他の人が参加する
    19:"KICKED_OUT_OF_GROUP"#グループから蹴られる
    25:"SEND_MESSAGE"#話す
    26:"RECEIVE_MESSAGE"#メッセージを受け取る


def using ():
    if op.type==13:
        op.param1="GROUP_ID"#グループ id
        op.param2=""
        op.param3="INVITED_PERSON_ID"#招待された人のid

    if op.type==16:
        pass

    if op.type==17:
        op.param1="GROUP_ID"#グループ id
        op.param2="PARTICPANT"#参加した人のid
