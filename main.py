# -*- coding: utf-8 -*-
from mafuLib.linepy import *
import time
from random import choice
nk_01=LINE("EA8xKhaj4LDzgCuMiR6b.TY1aqoynUFLD7kaCQdrgYW.U45aUdXqmNXvHWj0uEALMI5gso3aWaHZJqmmxkCjNo0=")
nk_02=LINE("EAhncCVu8fBuO0eC67y1.8RTMfj4dURGAbXXvXo8fyq.7SF7c00yh6TMAS41JBVDGT1UmWfdJOMb3ZnsiAlv6Ms=")
nk_03=LINE("EAy4tJCepwpalWRAhDN6.9zipI7oJeLytsrF5RlHATG.ZaM/At6gDvXUbgkMenShbS4tytxgA6cPcaduqWMC5kw=")
nk_04=LINE("EAYUvWVCeQ0mkSUublL7.nkhCcapFWhSsTBqy9h/BzW.lRbAaDHe12k554JSiTCibZSOuV2R5/wneBXMzTHidwY=")
nk_05=LINE("EArESYhqVuMI8ODyHGM0.A1h7+zOxzvQvRJNeX9HVCa.UgCCOzRoRagc/XI5n2tQaVZ+XDnAXIyh1b8iDewwU+w=")
nk_06=LINE("EAAHCUglPxK1o3aARiBc.yYAurc4LReXSlX+4BAueha.ZblkGVx+o8VtQYVlnrk5Je1xiEugo+DlokL5KgQ9W/0=")
nk_07=LINE("EA6522QZlyyDn7y5nDr0.UFV9+BogQx5C6POG197e8a.L9xTBhWyAUgurwZfsaE0UjM9yy3B2evUvB2VV2GEMP4=")
nk_08=LINE("EAAyycs1296xtWs9qXI5.DSPjpuhZ3sST/NA3WsOW1q.FJDk8Wfc2RD5RosRbKENZGB8sCZR6XFGVtxqekYwdX8=")
nk_01.log("Auth Token : " + str(nk_01.authToken))
nk_02.log("Auth Token : " + str(nk_02.authToken))
nk_03.log("Auth Token : " + str(nk_03.authToken))
nk_04.log("Auth Token : " + str(nk_04.authToken))
nk_05.log("Auth Token : " + str(nk_05.authToken))
nk_06.log("Auth Token : " + str(nk_06.authToken))
nk_07.log("Auth Token : " + str(nk_07.authToken))
nk_08.log("Auth Token : " + str(nk_08.authToken))

nks=[nk_01,nk_02,nk_03,nk_04,nk_05,nk_06,nk_07,nk_08]
lv_list=[]#生存nekosuke



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
G_list=[]
G_listName=[]
G_members=[]




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
                        elif op.param3 in B_list:
                            B_list.append(op.param2)
                            cnt=nk_01.getContact(op.param2)
                            B_listName.append(cnt.displayName)
                            nk_01.cancelGroupInvitation(op.param1,[op.param3])
                            nk_01.kickoutFromGroup(op.param1,[op.param2])


                    if op.type==15:
                        pass

                    if op.type==16:
                        G=nk_01.getGroup(op.param1)
                        G_list.append(G.id)
                        G_listName.append(G.name)
                        memid=[i.mid for i in G.members]
                        memid.remove(mid_01)
                        memid.remove(mid_02)
                        memid.remove(mid_03)
                        memid.remove(mid_04)
                        memid.remove(mid_05)
                        memid.remove(mid_06)
                        memid.remove(mid_07)
                        memid.remove(mid_08)
                        G_members.append(memid)
                        print(G_members)
                        print(G_list,G_listName)

                    if op.type==17:
                        G=nk_01.getGroup(op.param1)
                        gid=G.id
                        n=G_list.index(gid)
                        if op.param2 in B_list:
                            try:
                                nks[1].kickoutFromGroup(op.param1,[op.param2])
                                nks[1].sendMessage(op.param1,"blacklistuserを退会させました")
                            except:
                                continue
                        elif op.param2 in G_members[n]:
                            ct=nk_01.getContact(op.param2)
                            G=nk_01.getGroup(op.param1)
                            nk_01.sendMessage(op.param1,ct.displayName+"さん\nようこそ"+G.name+"へ")

                        else:
                            nk_01.sendMessage(op.param1,"メンバー登録をしてください")
                            nks[1].kickoutFromGroup(op.param1,[op.param2])

                    if op.type==19:
                        if op.param2 in B_list:
                            pass
                        else:
                            B_list.append(op.param2)
                        if op.param3 in nkids:
                            kicker=op.param2
                            n = nkids.index(op.param3)
                            lv_list.append(nks[n])
                            nks.pop(n)
                            nkids.remove(op.param3)
                            G=nks[1].getGroup(op.param1)
                            G.preventedJoinByTicket==False
                            nks[1].updateGroup(G)
                            T=nks[1].reissueGroupTicket(op.param1)
                            lv_list[0].acceptGroupInvitationByTicket(op.param1,T)
                            lv_list[0].kickoutFromGroup(op.param1,[kicker])
                            lv_list.pop(0)

                    if op.type==25:

                        msg=op.message
                        to=msg.to #groupid
                        _id=msg.id
                        cmd=msg.text

                        if cmd in ["test"]:
                            nk_01.sendMessage(to,"Hello")

                        if cmd in ["help"]:
                            allcmd='''===コマンド一覧===
┏━━━━━━━━━━━━━━━━━━
┣creator━作者名表示
┣nk:allin━nekosuke002~006参加
┣nk:allout━nekosuke002~006退会
┣leave:masternekosuke━nekosuke001退会
┣nk:makeURL━グループURL作成
┣nk:getGroup━グループの情報を取得
┣nk:allmember━グループのメンバー全員の名前とID表示
┗━━━━━━━━━━━━━━━━━━━

====================
☆☆☆☆☆☆☆create by hiroaki☆☆☆☆☆☆☆
====================
'''

                            nk_01.sendMessage(to,allcmd)

                        elif cmd in ["nk:allin"]:
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

                            nk_02.leaveGroup(to)
                            nk_03.leaveGroup(to)
                            nk_04.leaveGroup(to)
                            nk_05.leaveGroup(to)
                            nk_06.leaveGroup(to)
                            nk_07.leaveGroup(to)
                            nk_08.leaveGroup(to)

                        elif cmd in ["leave:masternekosuke"]:
                            nk_01.leaveGroup(to)

                        elif cmd in ["nk:makeURL"]:
                                G=nk_04.getGroup(to)
                                G.preventedJoinByTicket==False
                                nk_04.updateGroup(G)
                                T=nk_04.reissueGroupTicket(to)
                                nk_04.sendMessage(to,"https://line.me/ti/g/"+str(T))


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
                    if op.type==26:
                        msg=op.message
                        if msg.contentType==0:
                            to=msg.to #groupid
                            fr=msg._from#Sender
                            _id=msg.id
                            cmd=msg.text

                            if cmd in ["creator"]:
                                nk_01.sendMessage(to,"->create by ひろあき <-")
                                nk_02.sendMessage(to,"->create by ひろあき <-")
                                nk_03.sendMessage(to,"->create by ひろあき <-")
                                nk_04.sendMessage(to,"->create by ひろあき <-")
                                nk_05.sendMessage(to,"->create by ひろあき <-")
                                nk_06.sendMessage(to,"->create by ひろあき <-")
                                nk_07.sendMessage(to,"->create by ひろあき <-")
                                nk_08.sendMessage(to,"->create by ひろあき <-")

                            elif cmd in ["testcmd"]:
                                nk_01.sendMessage(to,"Hello World!")
                except:
                    print("ERROR!!")

                    import traceback
                    traceback.print_exc()

                finally:
                    nk_01.revision=max(op.revision,nk_01.revision)

                    #except (ZeroDivisionError, IOError):
                        #print("ERROR!!")
