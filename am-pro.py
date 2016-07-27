#!/usr/bin/python
import csv, sys
from sys import argv

script, infile, outfile = argv

# open csv file
instrCSV = csv.DictReader(open(infile))
target = open(outfile, 'w')
target.truncate()

target.write("""
/*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
A.G ARTICULATION MAPS PRO (Extra) v3.0  (ALL RIGHTS RESERVED)
Author: www.audiogrocery.com
Written by: Ivan Kovachev
Modified: March 03, 2015
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/

// * * * * * * * * *   P R E F E R E N C E S   * * * * * * * * *

" ::::::::::::::::::::  MIDI FILTER SETTINGS ::::::::::::::::::::                    "
var KS_Filter= -1; // Key Switch RBA filter switch (ON= 1; OFF= -1)
var PC_Filter= -1; // Program Change RBA filter switch (ON= 1; OFF= -1)
var CC_Filter= -1; // Control Change RBA filter switch (ON= 1; OFF= -1)

" ::::::::::::::::::  REMOTE CONTROL SETTINGS  ::::::::::::::::::                    "
var RC_Ch= 0 ; // Remote Midi Channel (ALL ASSIGNMENTS OFF=-1; Ch.ALL=0; ON=1-16)
var RC_PC= -1 ; // Remote Program Change OFF/ON (OFF= -1); (ON= 1)
var RC_CCnum= -1 ; // Remote CC Number (ON= 0-127; OFF= -1)
var RC_KSR_Min= -1; // Remote Key Switch MIN Number (OFF= -1)
var RC_KSR_Max= -1; // Remote Key Switch MAX Number (OFF= -1)
var RC_Offset= 0 ; // Remote Control Value Offset (OFF= 0; ON= +/- 1-127)
var RC_Thru= -1 ; // Remote Control THRU (ON= 1; OFF= -1)

" ::::::  ARTICULATION & PERFORMANCE MIDI CHANNEL SWITCHING  ::::::                  "
var PCH_SW=1;  // Performance MIDI Channel Switching (ON= 1; OFF= -1)
var STO= -1;    // Controllers Soft Takeover (ON= 1; OFF= -1)

" ::::::::::::::::::  MESSAGE ORDER SETTINGS  ::::::::::::::::::                     "
var MO_ON_OFF= -1 ; // Message Order Global ON/OFF switch (ON= 1; OFF= -1)
var MO=[
2,   // KS Note Number
1,   // Program Change Number
3,   // CC Number A
4,   // CC Number B
];
" ::::::::::::::::  PARAMETER NAME ASSIGNMENTS ::::::::::::::::                       "
var PN=[ // Type/assign custom parameter names inside the "  " below
"1. Articulation Maps",
"2. Mode",
"3. MIDI Channel",
"4. Key Switch Layer",
"5. Program Change Number",
"6. Control Change Number A",
"7. Control Change Value A",
"8. Control Change Number B",
"9. Control Change Value B",
"10. Send Current Map",
];
" :::::::::::::::  MIDI CHANNEL NAME ASSIGNMENTS  :::::::::::::::::                  "
var CN=[ // Type/replace the ------ with custom channel name "Ch.# ----- " below
""")

# count = 1
# for entry in instrCSV:
#     if entry['Special'] == 'E':
#         break
#     elif count == int(entry['MIDIchannel']):
#         target.write('"Ch.%s %s %s ", \n' % (count, entry['SampleLibrary'], entry['Name']))
#         count += 1

# count = 0
# while count <= 16:
#     count += 1
#     for entry in instrCSV:
#         if entry['Special'] == 'E':
#             break
#         elif count == int(entry['MIDIchannel']):
#             target.write('"Ch.%s %s %s ", \n' % (count, entry['SampleLibrary'], entry['Name']))
#             break
#         else:
#             continue

for i in range(1, 17):
    # print i
    for entry in instrCSV:
    #    print "current i: %s || entry: %s" % (i, entry)
        if entry['Special'] == 'E':
            continue
        elif i != int(entry['MIDIchannel']):
            continue
        elif i == int(entry['MIDIchannel']):
            target.write('"Ch.%s %s %s ", \n' % (i, entry['SampleLibrary'], entry['Name']))
            break
        else:
            break

target.write(""" ];
" :::::::::::  SEND CONTROLLER AFTER LOADING PROJECT  :::::::::::                     "
var CC_send=[[],[],[],[],]
CC_send[0][0]= 0 ;   // MIDI Channel. (Ch.All=0; Ch.1=1; Ch.2=2 etc)
CC_send[0][1]= -1 ;  // Assign the CC# to be sent after the Project loading (OFF= -1)
CC_send[0][2]= -1 ; // Control Change Default Value (OFF= -1)

CC_send[1][0]= 0 ;   // MIDI Channel. (Ch.All=0; Ch.1=1; Ch.2=2 etc)
CC_send[1][1]= -1 ; // Assign the CC# to be sent after the Project loading (OFF= -1)
CC_send[1][2]= -1 ; // Control Change Default Value (OFF= -1)

CC_send[2][0]= 0 ;   // MIDI Channel. (Ch.All=0; Ch.1=1; Ch.2=2 etc)
CC_send[2][1]= -1 ;  // Assign the CC# to be sent after the Project loading (OFF= -1)
CC_send[2][2]= -1 ; // Control Change Default Value (OFF= -1)

CC_send[3][0]= 0 ;   // MIDI Channel. (Ch.All=0; Ch.1=1; Ch.2=2 etc)
CC_send[3][1]= -1 ;  // Assign the CC# to be sent after the Project loading (OFF= -1)
CC_send[3][2]= -1 ; // Control Change Default Value (OFF= -1)

" ::::::::::::::::::::::  OTHER SETTINGS  ::::::::::::::::::::::                      "
var Auto_Latch= -1; // Enable/Disable KS Auto-Latching (ON= 1; OFF= -1)
var Auto_Latch_time= 30; // Transport Start Auto-Latch retriggering time (in msec)
var Ch_All= -1; // Global Channel Assignment of the Maps (OFF=-1; ON=Ch.1-16)
var KS_ON_Vel= 127; // Global Key Switch Velocity assignment(range 1-127)
var KS_OFF_time= 300; // Global Key Switch AUTO Note OFF time (in msec)
var KS2_ON_time= 25; // KS2 Note ON delay triggering time (in msec)
var KStoMAP= -1;   // Re-Map/Convert old MIDI KS into Maps TBA
var KS_ON_OFF= 1; // Send Key Switch via the KS Parameter/Menu (ON= 1; OFF= -1)

// ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
var AM=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],];var g6jk=127;for(var q=0; q<=g6jk; q++){AM[q][0]=-2;};
// ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



//================ A R T I C U L A T I O N   M A P S ================

""")
instrCSV = csv.DictReader(open(infile))
count = -1
for entry in instrCSV:
    if entry['Special'] == 'E':
        # End of CSV
        break
    if entry['Special'] == 'X':
        # Skip this entry
        continue
    else:
        count += 1
        target.write('AM[%s][0] = "%s.%s" ; // Articulation Map Name \n' % (count, count, entry['ArtMapName']))
        target.write('AM[%s][1] = %s ; // MIDI Channel 1-16 (KS OFF Ch.All= 0) \n' % (count, entry['MIDIchannel']))
        if entry['KS1name'][0].isalpha():
            target.write('AM[%s][2] = "%s" ; // KS1 Name or Note Number (OFF= -1) \n' % (count, entry['KS1name']))
        else:
            target.write('AM[%s][2] = %s ; // KS1 Name or Note Number (OFF= -1) \n' % (count, entry['KS1name']))
        target.write('AM[%s][3] = %s ; // Program Change Number (OFF= -1) \n' % (count, entry['ProgramChange']))
        target.write('AM[%s][4] = %s ; // CC Number A (OFF= -1) \n' % (count, entry['CCAnum']))
        target.write('AM[%s][5] = %s ; // CC Value A \n' % (count, entry['CCAvalue']))
        target.write('AM[%s][6] = %s ; // CC Number B (OFF= -1) \n' % (count, entry['CCBnum']))
        target.write('AM[%s][7] = %s ; // CC Value B \n' % (count, entry['CCBvalue']))
        target.write('AM[%s][8] = %s ; // KS Latch (OFF= -1; ON= 1) \n' % (count, entry['Kslatch']))
        if entry['KS2name'][0].isalpha():
            target.write('AM[%s][9] = "%s" ; // KS2 Name or Note Number (OFF= -1) \n' % (count, entry['KS2name']))
        else:
            target.write('AM[%s][9] = %s ; // KS2 Name or Note Number (OFF= -1) \n' % (count, entry['KS2name']))
        target.write('\n')

target.write("""// ----------- MAPS END ----------------------

//* * * * * * * * * *  C O D E  * * * * * * * * * *
var k2rt=[];for(i=0;i<=g6jk;i++){k2rt[i]=AM[i][0];}var PluginParameters=[PluginParameters={name:PN[0],type:"menu",valueStrings:k2rt,numberOfSteps:127,minValue:0,maxValue:127,defaultValue:0,},{name:PN[1],type:"menu",valueStrings:["OFF","MAPS AUTOM.  (Par. Change ON)","MAPS AUTOM.  (Par. Change OFF)","CONTINUOUS AUTOMATION","MIDI"],numberOfSteps:5,minValue:0,maxValue:4,defaultValue:1,},{name: PN[2],type:"menu",valueStrings:CN,numberOfSteps:16,minValue:0,maxValue:15,defaultValue:0,},{name: PN[3],
type:"menu",valueStrings:MIDI._noteNames,minValue:-1,maxValue:127,defaultValue:0,numberOfSteps:128,},{name:PN[4],type:"lin",minValue:-1,maxValue:127,numberOfSteps:128,defaultValue:-1,},{name:PN[5],type:"lin",minValue:-1,maxValue:127,numberOfSteps:128,defaultValue:-1,},{name:PN[6],type:"lin",minValue:0,maxValue:127,numberOfSteps:127,defaultValue:0,},{name:PN[7],type:"lin",minValue:-1,maxValue:127,numberOfSteps:128,defaultValue:-1,},{name:PN[8],type:"lin",minValue:0,maxValue:127,numberOfSteps:127,defaultValue:0,
},{name:PN[9],type:"menu",valueStrings:["OFF","ON",],numberOfSteps:2,minValue:0,maxValue:1,defaultValue:0,},];var MS=[];var l9qf=[0,25,50,75,100,125];for(i=0;i<=5;i++){if(MO[0]==i+1){MS[0]=l9qf[i];}if(MO[1]==i+1){MS[1]=l9qf[i];}if(MO[2]==i+1){MS[2]=l9qf[i];}if(MO[3]==i+1){MS[3]=l9qf[i];}}var i=0;var j2et=1;var n7gl=2;var l6pa=3;var p3fb=4;var p3fbV=5;var r5hz=6;var r5hzV=7;var m5fb=8;var n7gl_m=9;var p0av;var p0av2;var m5rh;var sg5n;var h7jk;var m3db=[0,0,0,0,0,0]; var gy8c=[];
var sr6h=0;var rb7j=[];var nw4t=[];var f6jn=["ALERT: Wrong KS1 Note Name in Map #","ALERT: Wrong KS2 Note Name in Map #","ALERT: Wrong Remote Control KS MIN Note Name!","ALERT: Wrong Remote Control KS MAX Note Name!"," !"];var b6sm=[];var j1eg=128;var cy5j=-1;var eh8n=-1;var rl2v=[];var le4g=1;var l3rh;var nr5h=[];var kl3h=0;var rt7m;for(i=0;i<=g6jk;i++){if(Ch_All>=j2et&&Ch_All<=16){AM[i][j2et]=Ch_All;}}NeedsTimingInfo=true;var bt6j=false;function ProcessMIDI(){if(Auto_Latch==1){var musicInfo=GetTimingInfo();if(!bt6j && musicInfo.playing){kl3h=1;
if(kl3h==1){gy7j();}}bt6j=musicInfo.playing;}}function k2eh(){SetParameter(2,AM[rb7j[0]][j2et]-1);rb7j[2]=GetParameter(2);if(AM[rb7j[0]][n7gl]>-1&&AM[rb7j[0]][n7gl]<j1eg){SetParameter(3,AM[rb7j[0]][n7gl]);rb7j[3]=GetParameter(3);l4rj();}if(AM[rb7j[0]][n7gl_m]>-1&&AM[rb7j[0]][n7gl_m]<j1eg){l4rj_m();}if(AM[rb7j[0]][l6pa]>-1){SetParameter(4,AM[rb7j[0]][l6pa]);rb7j[4]=GetParameter(4);rh7z();}if(AM[rb7j[0]][p3fb]>-1){SetParameter(5,AM[rb7j[0]][p3fb]);SetParameter(6,AM[rb7j[0]][p3fbV]);rb7j[5]=GetParameter(5);rb7j[6]=GetParameter(6);k2ws();
}if(AM[rb7j[0]][r5hz]>-1){SetParameter(7,AM[rb7j[0]][r5hz]);SetParameter(8,AM[rb7j[0]][r5hzV]);rb7j[7]=GetParameter(7);rb7j[8]=GetParameter(8);l2wf();}}function l4rj(){var note_on=new NoteOn;note_on.channel=rb7j[2]+1;note_on.pitch=rb7j[3];note_on.velocity=KS_ON_Vel;if(MO_ON_OFF==-1)note_on.send();else{note_on.sendAfterMilliseconds(MS[0]);}if(AM[rb7j[0]][m5fb]>0){gy8c[(AM[rb7j[0]][j2et]*j1eg)+rb7j[3]]=1;}else{var note_off=new NoteOff;note_off.channel=rb7j[2]+1;note_off.pitch=rb7j[3];note_off.velocity=0;if(AM[rb7j[0]][n7gl]==j1eg)note_off.send();
else{if(MO_ON_OFF==-1)note_off.sendAfterMilliseconds(KS_OFF_time);else{note_off.sendAfterMilliseconds(KS_OFF_time+MS[0])}}}p0av=rb7j[3];}function l4rj_m(){var note_on=new NoteOn;note_on.channel=AM[rb7j[0]][j2et];note_on.pitch=AM[rb7j[0]][n7gl_m];note_on.velocity=KS_ON_Vel;if(MO_ON_OFF==-1)note_on.sendAfterMilliseconds(KS2_ON_time);else{note_on.sendAfterMilliseconds(MS[0]);}if(AM[rb7j[0]][m5fb]>0){gy8c[(AM[rb7j[0]][j2et]*j1eg)+AM[rb7j[0]][n7gl_m]]=1;}else{var note_off=new NoteOff;note_off.channel=AM[rb7j[0]][j2et];note_off.pitch=AM[rb7j[0]][n7gl_m];
note_off.velocity=0;if(AM[rb7j[0]][n7gl_m]==j1eg)note_off.send();else{if(MO_ON_OFF==-1)note_off.sendAfterMilliseconds(KS_OFF_time);else{note_off.sendAfterMilliseconds(KS_OFF_time+MS[0])}}}}function be6y(){if(PCH_SW==-1&&AM[rb7j[0]][j2et]>0){for(i=0;i<j1eg;i++){if(gy8c[(AM[rb7j[0]][j2et]*j1eg)+i]==1){var note_off=new NoteOff;note_off.channel=AM[rb7j[0]][j2et];note_off.pitch=i;note_off.velocity=0;note_off.send();gy8c[(AM[rb7j[0]][j2et]*j1eg)+i]=0;}}}if(PCH_SW==1||AM[rb7j[0]][j2et]==0){for(i=j1eg;i<j1eg*17;i++){if(gy8c[i]==1 && i>j1eg){var note_off=new NoteOff;
note_off.channel=Math.floor(i/j1eg);note_off.pitch=i-(j1eg*Math.floor(i/j1eg));note_off.velocity=0;note_off.send();gy8c[i]=0;}}}}function rh7z(){if(rb7j[4]>-1){var Prg =new ProgramChange;Prg.channel=rb7j[2]+1;Prg.number=rb7j[4];if(MO_ON_OFF==-1)Prg.send();else{Prg.sendAfterMilliseconds(MS[1])}}m5rh=rb7j[4];}function k2ws(){if(rb7j[5]>-1){var ControlA=new ControlChange; ControlA.channel=rb7j[2]+1; ControlA.number=rb7j[5];ControlA.value=rb7j[6];if(MO_ON_OFF==-1)ControlA.send();else{ControlA.sendAfterMilliseconds(MS[2])}}sg5n=rb7j[6];}function l2wf(){if(rb7j[7]>-1){
var ControlB=new ControlChange;ControlB.channel=rb7j[2]+1;ControlB.number=rb7j[7];ControlB.value=rb7j[8];if(MO_ON_OFF==-1)ControlB.send();else{ControlB.sendAfterMilliseconds(MS[3])}}h7jk=rb7j[8];}function l4rj2(){if(AM[rb7j[0]][n7gl]>-1&&AM[rb7j[0]][n7gl]<j1eg){var note_on =new NoteOn;note_on.channel=AM[rb7j[0]][j2et];note_on.pitch=AM[rb7j[0]][n7gl];note_on.velocity=KS_ON_Vel;if(MO_ON_OFF==-1)note_on.send();else{note_on.sendAfterMilliseconds(MS[0]);}if(AM[rb7j[0]][m5fb]>0){gy8c[(AM[rb7j[0]][j2et]*j1eg)+AM[rb7j[0]][n7gl]]=1;
}else{var note_off=new NoteOff;note_off.channel=AM[rb7j[0]][j2et];note_off.pitch=AM[rb7j[0]][n7gl];note_off.velocity=0;if(AM[rb7j[0]][n7gl]==j1eg)note_off.send();else{if(MO_ON_OFF==-1)note_off.sendAfterMilliseconds(KS_OFF_time);else{note_off.sendAfterMilliseconds(KS_OFF_time+MS[0])}}}}if(AM[rb7j[0]][n7gl_m]>-1&&AM[rb7j[0]][n7gl_m]<j1eg){var note_on=new NoteOn;note_on.channel=AM[rb7j[0]][j2et];note_on.pitch=AM[rb7j[0]][n7gl_m];note_on.velocity=KS_ON_Vel;if(MO_ON_OFF==-1)note_on.sendAfterMilliseconds(KS2_ON_time);else{note_on.sendAfterMilliseconds(MS[0]);
}if(AM[rb7j[0]][m5fb]>0){gy8c[(AM[rb7j[0]][j2et]*j1eg)+AM[rb7j[0]][n7gl_m]]=1;}else{var note_off=new NoteOff;note_off.channel=AM[rb7j[0]][j2et];note_off.pitch=AM[rb7j[0]][n7gl_m];note_off.velocity=0;if(AM[rb7j[0]][n7gl_m]==j1eg)note_off.send();else{if(MO_ON_OFF==-1)note_off.sendAfterMilliseconds(KS_OFF_time);else{note_off.sendAfterMilliseconds(KS_OFF_time+MS[0])}}}}p0av=AM[rb7j[0]][n7gl];}function rh7z2(){if(AM[rb7j[0]][l6pa]>-1){var Prg=new ProgramChange;Prg.channel=AM[rb7j[0]][j2et];Prg.number=AM[rb7j[0]][l6pa];if(MO_ON_OFF==-1)Prg.send();
else{Prg.sendAfterMilliseconds(MS[1])}}m5rh=AM[rb7j[0]][l6pa];}function k2ws2(){if(AM[rb7j[0]][p3fb]>-1){var ControlA=new ControlChange; ControlA.channel=AM[rb7j[0]][j2et];ControlA.number=AM[rb7j[0]][p3fb];ControlA.value=AM[rb7j[0]][p3fbV];if(MO_ON_OFF==-1)ControlA.send();else{ControlA.sendAfterMilliseconds(MS[2])}}sg5n=AM[rb7j[0]][p3fbV];}function l2wf2(){if(AM[rb7j[0]][r5hz]>-1){var ControlB=new ControlChange;ControlB.channel=AM[rb7j[0]][j2et];ControlB.number=AM[rb7j[0]][r5hz];ControlB.value=AM[rb7j[0]][r5hzV];if(MO_ON_OFF==-1)ControlB.send();
else{ControlB.sendAfterMilliseconds(MS[3])}}h7jk=AM[rb7j[0]][r5hzV];}var p3dg;for(i=0;i<=g6jk;i++){if(AM[i][0]!=-2){p3dg=i;}}var a=-1;var j=0;while(a<j1eg&&j<=g6jk){if(AM[j][n7gl]==-1||AM[j][n7gl]==j1eg){a=-1;j++;}if(MIDI._noteNames[a]==AM[j][n7gl]||AM[j][n7gl]==a){AM[j][n7gl]=a;a=-1;j++;}a++;}if(j<=p3dg){Trace(f6jn[0]+j+f6jn[4]);};a=-1;j=0; while(a<j1eg&&j<=g6jk){if(AM[j][n7gl_m]==-1||AM[j][n7gl_m]==j1eg){a=-1;j++;}if(MIDI._noteNames[a]==AM[j][n7gl_m]||AM[j][n7gl_m]==a){AM[j][n7gl_m]=a;a=-1;j++;}a++;}if(j<=p3dg){Trace(f6jn[1]+j+f6jn[4]);};
a=0;j=0;for(i=0;i<j1eg;i++){if(MIDI._noteNames[i]==RC_KSR_Min||[i]==RC_KSR_Min){RC_KSR_Min=i;a=-2;}if(MIDI._noteNames[i]==RC_KSR_Max||[i]==RC_KSR_Max){RC_KSR_Max=i;j=-2;}}if(a==0&&RC_KSR_Min!=-1){Trace(f6jn[2]);}if(j==0&&RC_KSR_Max!=-1){Trace(f6jn[3]);}function gy7j(){for(i=j1eg;i<j1eg*17;i++){if(gy8c[i]==1&&i>j1eg){var note_on=new NoteOn;note_on.channel=Math.floor(i/j1eg);note_on.pitch=i-(j1eg*Math.floor(i/j1eg));note_on.velocity=KS_ON_Vel;if(MO_ON_OFF==-1)note_on.sendAfterMilliseconds(Auto_Latch_time);else{note_on.sendAfterMilliseconds(MS[0]+Auto_Latch_time);}}}
}function ParameterChanged(param,value){rb7j[param]=value;for (i=0;i<=3;i++){if(CC_send[i][1]>-1&&sr6h==0){var cc=new ControlChange;for (var k=1;k<=16;k++){if(CC_send[i][0]==0){cc.channel=k;cc.number=CC_send[i][1];cc.value=CC_send[i][2];}else{cc.channel=CC_send[i][0];cc.number=CC_send[i][1];cc.value=CC_send[i][2];}cc.send();}}}sr6h=1;if(param==0){if(STO==1){if(eh8n!=AM[rb7j[0]][j2et]){cy5j=eh8n;}eh8n=AM[rb7j[0]][j2et];if(cy5j!=-1){if(AM[rb7j[0]][j2et]!=cy5j){for (i=0;i<j1eg;i++){b6sm[(l3rh*j1eg)+i]=nr5h[i];rl2v[i]=1;}}}}kl3h=0;
if(rb7j[1]==1){be6y();k2eh();}if(rb7j[1]==2){be6y();l4rj2();rh7z2();k2ws2();l2wf2();}}if(param==3&&KS_ON_OFF==1){if(rb7j[1]==1&&m3db[0]==1&&rb7j[3]!=p0av||rb7j[1]==3 && m3db[0]==1){be6y();l4rj();}m3db[0]=1;}if(param==4){if(rb7j[1]==1&&m3db[1]==1&&rb7j[4]!=m5rh||rb7j[1]==3&&m3db[1]==1){rh7z();}m3db[1]=1;}if(param==6){if(rb7j[1]==1&&m3db[2]==1&&rb7j[6]!=sg5n||rb7j[1]==3&&m3db[2]==1){k2ws();}m3db[2]=1;}if(param==8){if(rb7j[1]==1&&m3db[3]==1&&rb7j[8]!=h7jk||rb7j[1]==3&&m3db[3]==1){l2wf();}m3db[3]=1;}if(param==9){if(value==0&&rb7j[1]==1){k2eh();}if(rb7j[9]==1&&rb7j[1]==1){
k2eh();SetParameter(9,0);}if(rb7j[1]>1){l4rj2();rh7z2();k2ws2();l2wf2();SetParameter(9,0);}}}function HandleMIDI(e){if(GetParameter(PN[1])==2){if(RC_Ch==0){rt7m=e.channel;}if(RC_Ch>=1&&RC_Ch<=16){rt7m=RC_Ch;}if(e instanceof Note&&rt7m==e.channel&&e.pitch>=RC_KSR_Min&&e.pitch<=RC_KSR_Max){SetParameter(PN[0],e.pitch-RC_KSR_Min+RC_Offset);if(RC_Thru==-1){return undefined;}}if(e instanceof ProgramChange&&rt7m==e.channel&&RC_PC==1){SetParameter(PN[0],e.number+RC_Offset);if(RC_Thru==-1){return undefined;}}
if(e instanceof ControlChange&&rt7m==e.channel&&RC_CCnum>-1&&RC_CCnum==e.number){SetParameter(PN[0],e.value+RC_Offset);if(RC_Thru==-1){return undefined;}}}if(e instanceof NoteOn){if(rb7j[1]<3&&KS_Filter==1){for(i=0;i<=g6jk;i++){if(e.channel==AM[i][j2et]&&e.pitch==AM[i][n7gl]||e.channel==AM[i][j2et]&&e.pitch==AM[i][n7gl_m]){return undefined;}}}if(rb7j[1]==2&&KStoMAP==1){for(i=0;i<=g6jk;i++){if(e.channel==AM[i][j2et]&&e.pitch==AM[i][n7gl]||e.channel==AM[i][j2et]&&e.pitch==AM[i][n7gl_m]){SetParameter(0, i);return undefined;
}}}if(rb7j[1]==4&&e.channel==rb7j[2]+1){SetParameter(3,e.pitch)}if(PCH_SW==1){if(rb7j[1]==1)nw4t[e.pitch]=rb7j[2]+1;else{nw4t[e.pitch]=AM[rb7j[0]][j2et];}}}if(e instanceof ControlChange){if(rb7j[1]<3&&CC_Filter==1){for(i=0;i<=g6jk;i++){if(e.channel==AM[i][j2et]&&e.number==AM[i][p3fb]||e.channel==AM[i][j2et]&&e.number==AM[i][r5hz]){return undefined;}}}if(rb7j[1]==4&&e.channel==rb7j[2]+1){if(rb7j[5]==e.number){SetParameter(6,e.value);}if(rb7j[7]==e.number){SetParameter(8,e.value);}}}
if(e instanceof ProgramChange){if(rb7j[1]<3&&PC_Filter==1){for(i=0;i<=g6jk;i++){if(e.channel==AM[i][j2et]&&e.number==AM[i][l6pa]){return undefined;}}}if(rb7j[1]==4&&e.channel==rb7j[2]+1&&rb7j[4]>-1){SetParameter(4,e.number);}}if(PCH_SW==1){if(e instanceof NoteOff)e.channel=nw4t[e.pitch];else{if(rb7j[1]==1)e.channel=rb7j[2]+1;else{e.channel=AM[rb7j[0]][j2et];}}if(e instanceof ControlChange&&STO==1){if(e.channel!=cy5j&&rl2v[e.number]==1){if(b6sm[(e.channel*j1eg)+e.number]>=0){if(b6sm[(e.channel*j1eg)+e.number]!=e.value)le4g=0;else{le4g=1;
rl2v[e.number]=0;}}}l3rh=e.channel;nr5h[e.number]=e.value;if(le4g==0){return undefined;}}}e.send();}
// End Code
 """)

target.close()

# simple printing version
# count = -1
# for entry in instrCSV:
#     if entry['End'] == 'E':
#         break
#     else:
#         count += 1
#         print'AM0[%s][0] = "%s.%s" ; // Articulation Map Name ' % (count, count, entry['ArtMapName'])
#         print'AM0[%s][1] = %s ; // MIDI Channel 1-16 (KS OFF Ch.All= 0) ' % (count, entry['MIDIchannel'])
#         print'AM0[%s][2] = "%s" ; // KS1 Name or Note Number (OFF= -1) ' % (count, entry['KS1name'])
#         print'AM0[%s][3] = %s ; // Program Change Number (OFF= -1) ' % (count, entry['ProgramChange'])
#         print'AM0[%s][4] = %s ; // CC Number A (OFF= -1) ' % (count, entry['CCAnum'])
#         print'AM0[%s][5] = %s ; // CC Value A ' % (count, entry['CCAvalue'])
#         print'AM0[%s][6] = %s ; // CC Number B (OFF= -1) ' % (count, entry['CCBnum'])
#         print'AM0[%s][7] = %s ; // CC Value B ' % (count, entry['CCBvalue'])
#         print'AM0[%s][8] = %s ; // KS Latch (OFF= -1; ON= 1) ' % (count, entry['Kslatch'])
#         print'AM0[%s][9] = "%s" ; // KS2 Name or Note Number (OFF= -1)' % (count, entry['KS2name'])
#         print ''
