# -*- coding: utf-8 -*-
from mafuLib.linepy import *
import time
from random import choice
nk_01=LINE("")
nk_02=LINE("")
nk_03=LINE("")
nk_04=LINE("")
nk_05=LINE("")
nk_06=LINE("")
nk_07=LINE("")
nk_08=LINE("")

nk_01.log("Auth Token : " + str(nk_01.authToken))
nk_02.log("Auth Token : " + str(nk_02.authToken))
nk_03.log("Auth Token : " + str(nk_03.authToken))
nk_04.log("Auth Token : " + str(nk_04.authToken))
nk_05.log("Auth Token : " + str(nk_05.authToken))
nk_06.log("Auth Token : " + str(nk_06.authToken))
nk_07.log("Auth Token : " + str(nk_07.authToken))
nk_08.log("Auth Token : " + str(nk_08.authToken))

nks=[nk_01,nk_02,nk_03,nk_04,nk_05,nk_06,nk_07,nk_08]



mid_01=nk_01.getProfile().mid
mid_02=nk_02.getProfile().mid
mid_03=nk_03.getProfile().mid
mid_04=nk_04.getProfile().mid
mid_05=nk_05.getProfile().mid
mid_06=nk_06.getProfile().mid
mid_07=nk_07.getProfile().mid
mid_08=nk_08.getProfile().mid



nkids=[mid_01,mid_02,mid_03,mid_04,mid_05,mid_06,mid_07,mid_08]

B_list=[]
B_listName=[]
G_list=['ceb7c7b0a70448e2ee11ba8fc79ebd23e', 'cd6553fd0f58641d883934dfeee58efe0', 'c9fd315c4cc333cdd66943d4c568d506e', 'ceca69d0d1b0303047913a241cc0c9365', 'ca72e9807147f1c827471306ca74ee223']
G_listName=['npcaの部分集合42468759872501368450', 'sample', 'sample(2)', 'NPCA76回生','sample(3)']
user_list=['u2b9cfdb21068feeb5be01b9b41e29243','u6b51fbfd9a17655a95ae39c4c7d86f70','uf2bb66149e03bab81a071c55c4ef0561','u34a1dc0803dfc07b12b5b418f47f9b67','ub72d4040e60db9f95deca01ca83446c']




while True:
    try:
        ops_nk01=nk_01.poll.fetchOperations(nk_01.revision,50)


    except:
        continue

    if ops_nk01!=None:
            for op in ops_nk01:
                try:
                    if op.type==0:
                        pass
                    if op.type==13:
                        if op.param3==mid_01:
                            nk_01.acceptGroupInvitation(op.param1)

                    if op.type==15:
                        print(op.param1)
                        print(op.param2)

                        if op.param2==mid_02:
                            print("SUCCESS")
                            nk_01.inviteIntoGroup(op.param1,[mid_02])



                    if op.type==16:

                        G=nk_01.getGroup(op.param1)
                        G_list.append(G.id)
                        G_listName.append(G.name)
                        print(G_list,G_listName)

                    if op.type==17:
                        if op.param2 in B_list:
                            try:
                                nk_01.kickoutFromGroup(op.param1,[op.param2])
                                nk_01.sendMessage(op.param1,"blacklistuserを退会させました")
                                nk_02.kickoutFromGroup(op.param1,[op.param2])
                                nk_02.sendMessage(op.param1,"blacklistuserを退会させました")
                                nk_03.kickoutFromGroup(op.param1,[op.param2])
                                nk_03.sendMessage(op.param1,"blacklistuserを退会させました")
                                nk_04.kickoutFromGroup(op.param1,[op.param2])
                                nk_04.sendMessage(op.param1,"blacklistuserを退会させました")
                                nk_05.kickoutFromGroup(op.param1,[op.param2])
                                nk_05.sendMessage(op.param1,"blacklistuserを退会させました")
                                nk_06.kickoutFromGroup(op.param1,[op.param2])
                                nk_06.sendMessage(op.param1,"blacklistuserを退会させました")
                                nk_07.kickoutFromGroup(op.param1,[op.param2])
                                nk_07.sendMessage(op.param1,"blacklistuserを退会させました")
                                nk_08.kickoutFromGroup(op.param1,[op.param2])
                                nk_08.sendMessage(op.param1,"blacklistuserを退会させました")
                            except:
                                continue
                        elif op.param2 in nkids:
                            ct=nk_01.getContact(op.param2)
                            nk_01.sendMessage(op.param1,"Hello!   " + ct.displayName)

                    if op.type==19:
                        if op.param2 in B_list:
                            pass
                        else:
                            B_list.append(op.param2)
                        if op.param3 in nkids:
                            for k in range(len(nks)):
                                try:
                                    G=nks[k].getGroup(op.param1)
                                    G.preventedJoinByTicket=False
                                    nks[k].updateGroup(G)
                                    T=nks[k].reissueGroupTicket(op.param1)
                                    nks[k].kickoutFromGroup(op.param1,[op.param2])
                                    try:
                                        for f in range(len(nks)):
                                            nks[f].acceptGroupInvitationByTicket(op.param1,T)
                                    except:
                                        continue
                                except:
                                    continue
                    if op.type==25:
                        print(str(op.param1))
                        print(str(op.param2))
                        print(str(op.param3))
                        msg=op.message
                        to=msg.to #groupid
                        _id=msg.id
                        cmd=msg.text

                        if cmd in ["test"]:
                            nk_01.sendMessage(to,"Hello")

                    if op.type==26:
                        msg=op.message
                        if msg.contentType==0:
                            to=msg.to #groupid
                            fr=msg._from#Sender
                            _id=msg.id
                            cmd=msg.text

                            if cmd in ["help"]:
                                if fr in user_list:
                                    allcmd="┏━━━━━━━━━━━━━━━━━━━\n┣creator━作者名表示\n┣nk:allin━nekosuke002~006参加\n┣nk:allout━nekosuke002~006退会\n┣leave:masternekosuke━nekosuke001退会\n┣nk:makeURL━グループURL作成\n┣nk:getGroup━グループの情報を取得\n┣nk:allmember━グループのメンバー全員の名前とID表示\n┗━━━━━━━━━━━━━━━━━━━"
                                    nk_01.sendMessage(to,"コマンド一覧\n"+allcmd+"\n\n====================\n\n☆☆☆☆☆☆☆create by hiroaki☆☆☆☆☆☆☆\n\n====================")
                            elif cmd in ["creator"]:
                                nk_01.sendMessage(to,"->create by ひろあき <-")
                                nk_02.sendMessage(to,"->create by ひろあき <-")
                                nk_03.sendMessage(to,"->create by ひろあき <-")
                                nk_04.sendMessage(to,"->create by ひろあき <-")
                                nk_05.sendMessage(to,"->create by ひろあき <-")
                                nk_06.sendMessage(to,"->create by ひろあき <-")
                                nk_07.sendMessage(to,"->create by ひろあき <-")
                                nk_08.sendMessage(to,"->create by ひろあき <-")

                            elif cmd in ["nk:allin"]:
                                if fr in user_list:
                                    print("True")
                                    G=nk_01.getGroup(to)
                                    G.preventedJoinByTicket=False
                                    nk_01.updateGroup(G)
                                    T=nk_01.reissueGroupTicket(to)
                                    nk_02.acceptGroupInvitationByTicket(to,T)
                                    nk_03.acceptGroupInvitationByTicket(to,T)
                                    nk_04.acceptGroupInvitationByTicket(to,T)
                                    nk_05.acceptGroupInvitationByTicket(to,T)
                                    nk_06.acceptGroupInvitationByTicket(to,T)
                                    nk_07.acceptGroupInvitationByTicket(to,T)
                                    nk_08.acceptGroupInvitationByTicket(to,T)


                            elif cmd in ["nk:allout"]:
                                if fr in user_list:
                                    nk_02.leaveGroup(to)
                                    nk_03.leaveGroup(to)
                                    nk_04.leaveGroup(to)
                                    nk_05.leaveGroup(to)
                                    nk_06.leaveGroup(to)
                                    nk_07.leaveGroup(to)
                                    nk_08.leaveGroup(to)

                            elif cmd in ["leave:masternekosuke"]:
                                if fr in user_list:
                                    nk_01.leaveGroup(to)

                            elif cmd in ["nk:makeURL"]:
                                if fr in user_list:
                                    G=nk_04.getGroup(to)
                                    G.preventedJoinByTicket==False
                                    nk_04.updateGroup(G)
                                    T=nk_04.reissueGroupTicket(to)
                                    nk_04.sendMessage(to,"https://line.me/ti/g/"+str(T))

                            elif cmd in ["blacklist"]:
                                print(B_list)
                                print(B_listName)
                                m = len(B_list)
                                print(m)
                                tx="BLACK LIST\n"
                                print(tx)
                                for k in range(m):
                                    tx = tx + B_listName[k] +"\t\t\t"+str(B_list[k])+"\n"
                                nk_01.sendMessage(to,tx)


                            elif cmd in ["nk:getGroup"]:
                                if fr in user_list:
                                    G=nk_02.getGroup(to)
                                    if G.id in G_list:

                                        n=G_list.index(G.id)

                                        nk_02.sendMessage(to,"グループ名:"+G_listName[n]+"\nGroupID:"+G_list[n])

                                    else:
                                        G_list.append(G.id)
                                        G_listName.append(G.name)

                                        n=G_list.index(G.id)

                                        nk_02.sendMessage(to,"グループ名:"+G_listName[n]+"\nGroupID:"+G_list[n])

                            elif cmd in ["nk:allmember"]:
                                if fr in user_list:
                                    G=nk_02.getGroup(to)
                                    memid=[i.mid for i in G.members]
                                    names=[i.displayName for i in G.members]
                                    m=len(memid)
                                    print("n")
                                    Roster = "メンバー一覧\n"#名簿
                                    print("n")
                                    for j in range(m):
                                        Roster = Roster + names[j] + "\n" + "\t" + "\t"+ "\t"+ "\t"+ "\t"+ "ID : " + str(memid[j]) + "\n"

                                    nk_02.sendMessage(to,Roster)
                                    #for j in range(m):
                                        #nk_02.sendMessage(to,name[j]+"\nID : "+str(memid[j]))
                            elif cmd in ["nk:allgroup"]:
                                for i in range(len(G_list)):
                                    nk_02.sendMessage(to,G_listName[i])

                            elif cmd in ["nk:sp"]:
                                st=[]
                                en=[]
                                m=len(nks)
                                for i in range(m):
                                    nks[i].sendMessage(to,".")
                                    st.append(time.time())
                                for j in range(m):
                                    en.append(time.time())
                                    nks[j].sendMessage(to,"速度は\n%ssec"%(en[j]-st[j]))

                            else:
                                ct=nk_01.getContact(fr)
                                G=nk_01.getGroup(to)
                                talk="["+G.name+":"+ct.displayName+"] : " + cmd
                                nk_01.sendMessage('c9fd315c4cc333cdd66943d4c568d506e',talk)





                except:
                    print("ERROR!!")

                    import traceback
                    traceback.print_exc()

                finally:
                    nk_01.revision=max(op.revision,nk_01.revision)

                    #except (ZeroDivisionError, IOError):
                        #print("ERROR!!")
