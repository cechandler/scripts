#!/usr/bin/python
import csv, sys
from sys import argv

# script, infile, outfile = argv
script, infile = argv

# open csv file
instrCSV = csv.DictReader(open(infile))

for entry in instrCSV:
    # outfile = entry['SampleLibrary']+' '+entry['Name']
    if entry['Family'] is not None:
        outfile = entry['SampleLibrary']+' - '+entry['Family']+' - '+entry['Name']+'.js'
    else:
        outfile = entry['SampleLibrary']+' '+entry['Name']+'.js'
    break
target = open(outfile, 'w')
target.truncate()

target.write("""/*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
AG ARTICULATION SWITCHER v4.0  (ALL RIGHTS RESERVED)
Author: www.audiogrocery.com
Written by: Ivan Kovachev
Modified: November 17, 2015
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/

/* :::::::::::::  A R T I C U L A T I O N   M A P S  :::::::::::::                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              =========================================*/var AM=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],];var MODE=1;var PN=[];var kl9r=256;for(var q=0; q<=kl9r; q++){AM[q][0]=-2;};var RC;var RC_Offset;var RC_Num;var RC_Thru;var KS_Filter;var PC_Filter;var CC_Filter;var STO;var MO_ON_OFF;var MO=[];var CC_send=[[],[],[],[],];var Auto_Latch;var Auto_Latch_time;var Ch_All;var KS_ON_Vel;var EXS=[];

// MODE=1 if using multi-timbral mode (multiple MIDI chns with kontakt)
// MODE=2 if using mono-timbral mode

MODE=2;

""")

for i in range(1, 17):
    # print i
    for entry in instrCSV:
    #    print "current i: %s || entry: %s" % (i, entry)
        if entry['Special'] == 'E':
            continue
        elif i != int(entry['MIDIchannel']):
            continue
        elif i == int(entry['MIDIchannel']):
            target.write('PN[%s]="%s %s"; \n' % (i, entry['SampleLibrary'], entry['Name']))
            break
        else:
            break

target.write('\n')

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

target.write("""
// :::::::::::::::::::::::::  MAPS END  ::::::::::::::::::::::::::


// * * * * * * * * *   P R E F E R E N C E S   * * * * * * * * *

" ::::::::::::::::::  REMOTE CONTROL SETTINGS  ::::::::::::::::::                    "
RC= 1 ;          // Remote Control ON/OFF (ON= 1; OFF= -1)
RC_Num= 118;    // Remote Control Number
RC_Offset= 0 ; // Remote Control Value Offset (OFF= 0; ON= +/- 1 to 127)
RC_Thru= -1 ; // Remote Control THRU (ON= 1; OFF= -1)

" ::::::::::::::::::::  MIDI FILTER SETTINGS ::::::::::::::::::::                    "
KS_Filter= -1; // Key Switch RBA Filter (ON= 1; OFF= -1)
PC_Filter= -1; // Program Change RBA Filter (ON= 1; OFF= -1)
CC_Filter= -1; // Control Change RBA Filter (ON= 1; OFF= -1)

" :::::::::::  MONO TIMBRAL MODE (TBA)  :::::::::::                     "
STO= -1;    // Controllers Soft Takeover (ON= 1; OFF= -1)

" ::::::::::::::::::  MESSAGE ORDER SETTINGS  ::::::::::::::::::                     "
MO_ON_OFF= -1 ; // Message Order Global ON/OFF switch (ON= 1; OFF= -1)
MO=[
4,   // KS Note Number
1,   // Program Change Number
2,   // CC Number A
3,   // CC Number B
];

" :::::::::::  SEND CONTROLLER AFTER LOADING PROJECT  :::::::::::                     "
CC_send[0][0]= 0 ;   // MIDI Channel. (Ch.All=0; Ch.1=1; Ch.2=2 etc)
CC_send[0][1]= -1 ;  // Assign the CC# to be sent after the Project loading (OFF= -1)
CC_send[0][2]= 0 ; // Control Change Value

CC_send[1][0]= 0 ;   // MIDI Channel. (Ch.All=0; Ch.1=1; Ch.2=2 etc)
CC_send[1][1]= -1  ; // Assign the CC# to be sent after the Project loading (OFF= -1)
CC_send[1][2]= 0 ; // Control Change Value

CC_send[2][0]= 0 ;   // MIDI Channel. (Ch.All=0; Ch.1=1; Ch.2=2 etc)
CC_send[2][1]= -1 ;  // Assign the CC# to be sent after the Project loading (OFF= -1)
CC_send[2][2]= 0 ; // Control Change Value

CC_send[3][0]= 0 ;   // MIDI Channel. (Ch.All=0; Ch.1=1; Ch.2=2 etc)
CC_send[3][1]= -1 ;  // Assign the CC# to be sent after the Project loading (OFF= -1)
CC_send[3][2]= 0 ; // Control Change Value

" ::::::::::::::::::::::  OTHER SETTINGS  ::::::::::::::::::::::                      "
Auto_Latch= -1; // Enable/Disable KS Auto-Latching (ON= 1; OFF= -1)
Auto_Latch_time= 50; // Transport Start Auto-Latch retriggering time (in msec)
Ch_All= -1;  // Global Channel Assignment of the Maps (OFF=-1; ON=Ch.1-16)
KS_ON_Vel= 127; // Global Key Switch Velocity assignment(range 1-127)
KS_OFF_time= 300; // Global Key Switch AUTO Note OFF time (in msec)
KS2_ON_time= 55; // KS2 Note ON delay triggering time (in msec)
PC_Offset= 0; // Program Change Offset
CCa_Offset= 0; // CC_A Offset
CCb_Offset= 0; // CC_B Offset
Link_Plg= -1;  // Link AG Artic Switcher plugins(OFF=-1; ON=1)


//* * * * * * * * * * * *  C O D E  * * * * * * * * * * * *

var i=0;var z=0;var y=0;var df4k=[];var rt4f=[];var gh4l=1;var et4m=2;var wt7h=3;var ja3b=4;var ja3bV=5;var oa4x=6;var oa4xV=7;var tv9a=8;var et4m_m=9;var pw5z=[];var pv3k=0;var bi2s=[];var le4c=[];var bi2s2=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],];var mi7g;var oa3n;var is3l=["ALERT: Wrong KS1 Note Name in Map #","ALERT: Wrong KS2 Note Name in Map #","ALERT: Wrong Remote Control KS MIN Note Name!","ALERT: Wrong Remote Control KS MAX Note Name!"," !"];
var ks1f=[];var ga3m=128;var ic8f=-1;var ow8m=-1;var kq4b=[];var hy0l=1;var eh5k;var sw7k=[];var oq1g=0;var bw5l= -1;var lw1z=[];var pv7g=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],];var mq2j=0;var iz4d=0;var os6k=[];var uc5d=[];var uc5dB=[];var lx3j=1;var pv4h=0;var id2f;var ke5v=[];var et6m;var lq8m;for(i=0;i<=kl9r;i++){if(AM[i][0]!=-2){lq8m=i;}}var a=-1; var j=0; while(a<ga3m&&j<=kl9r){if(AM[j][et4m]==-1||AM[j][et4m]==ga3m){a=-1;j++;}
if(MIDI._noteNames[a]==AM[j][et4m]||AM[j][et4m]==a){AM[j][et4m]=a;a=-1;j++;}a++;}if(j<=lq8m){Trace(is3l[0]+j+is3l[4]);};a=-1;j=0;while(a<ga3m&&j<=kl9r){if(AM[j][et4m_m]==-1||AM[j][et4m_m]==ga3m){a=-1;j++;}if(MIDI._noteNames[a]==AM[j][et4m_m]||AM[j][et4m_m]==a){AM[j][et4m_m]=a;a=-1;j++;}a++;}if(j<=lq8m){Trace(is3l[1]+j+is3l[4]);};et6m=MODE;if(et6m==4){KS2_ON_time=0;}if(et6m==2||et6m==4)bw5l=1;else{bw5l=-1}var PluginParameters=[];for(i=0;i<=17;i++){uc5dB[i]=0;os6k[i]=0;}
for(i=0;i<=kl9r;i++){uc5dB[iz4d]=AM[i][gh4l];if(AM[i][1]!=pv4h){iz4d++;uc5dB[iz4d]=AM[i][gh4l];pv4h=AM[i][1];}for(z=1;z<=17;z++){if(AM[i][1]==z){pv7g[z-1][os6k[z]]=AM[i][0];bi2s2[z-1][os6k[z]]=i;os6k[z]++;}}}var me5t=1;z=0;for(i=0;i<=16;i++){if(uc5dB[i]==me5t){uc5d[z]=me5t;z++;}if(i==16){me5t++;i=-1;}if(me5t==17){i=20;}}if(et6m==1){for(i=0;i<iz4d-1;i++){PluginParameters.push({name:"Ch."+uc5d[i]+"  "+PN[uc5d[i]],type:"menu",valueStrings:pv7g[uc5d[i]-1],
numberOfSteps:127,minValue:0,maxValue:127,defaultValue:0});ke5v[i]="Ch."+uc5d[i]+"  "+PN[uc5d[i]];}}if(et6m==2||et6m==4){for(i=0;i<=kl9r;i++){if(i!=AM[i][0]){lw1z[i]=AM[i][0];}}PluginParameters.push({name: PN[1],type:"menu",valueStrings:lw1z,numberOfSteps:127,minValue:0,maxValue:127,defaultValue:0,});}if(et6m==3){PluginParameters.push({name:PN[1],type:"menu",valueStrings:EXS,numberOfSteps:127,minValue:0,maxValue:127,defaultValue:0,});}
z=AM[0][gh4l];for(i=0;i<=kl9r;i++){if(AM[i][gh4l]!=z){rt4f[z]=i-y;z=AM[i][gh4l];y=i;}if(AM[i][et4m]!=-1||AM[i][wt7h]!=-1||AM[i][ja3b]!=-1||AM[i][oa4x]!=-1||AM[i][et4m_m]!=-1)df4k[z]=1;else{df4k[z]=0;}} var MS=[];var dly=[0,25,50,75,100,125];for(i=0;i<=5;i++){if(MO[0]==i+1){MS[0]=dly[i];}if(MO[1]==i+1){MS[1]=dly[i];}if(MO[2]==i+1){MS[2]=dly[i];}if(MO[3]==i+1){MS[3]=dly[i];}}for(i=0;i<=kl9r;i++){if(Ch_All>=1&&Ch_All<=16){AM[i][gh4l]=Ch_All;}}NeedsTimingInfo=true;var wasplaying=false;function ProcessMIDI() {
if(Auto_Latch==1){var musicInfo=GetTimingInfo();if(!wasplaying&&musicInfo.playing){oq1g=1;if(oq1g==1){pa3m();}}wasplaying=musicInfo.playing;}}function be6k(){oq1g=0;fh4l();dn8s();vj3l();bw7l();lq3b();sf4h();}function fh4l(){ if(bw5l==-1&&AM[mi7g][gh4l]>0){for(i=0;i<ga3m;i++){if(pw5z[(AM[mi7g][gh4l]*ga3m)+i]==1){var note_off=new NoteOff;note_off.channel=AM[mi7g][gh4l];note_off.pitch=i;note_off.velocity=0;note_off.send();pw5z[(AM[mi7g][gh4l]*ga3m)+i]=0;}}}
if(bw5l==1||AM[mi7g][gh4l]==0){for(i=ga3m;i<ga3m*17;i++){if(pw5z[i]==1&&i>ga3m){var note_off=new NoteOff;note_off.channel=Math.floor(i/ga3m);note_off.pitch=i-(ga3m*Math.floor(i/ga3m));note_off.velocity=0;note_off.send();pw5z[i]=0;}}}}function dn8s(){if(AM[mi7g][et4m]>-1&&AM[mi7g][et4m]<ga3m){var note_on=new NoteOn;note_on.channel=AM[mi7g][gh4l];note_on.pitch=AM[mi7g][et4m];note_on.velocity=KS_ON_Vel;if(MO_ON_OFF==-1)note_on.send();else{note_on.sendAfterMilliseconds(MS[0]);}if(AM[mi7g][tv9a]>0)
{pw5z[(AM[mi7g][gh4l]*ga3m)+AM[mi7g][et4m]]=1;}else{var note_off=new NoteOff;note_off.channel=AM[mi7g][gh4l];note_off.pitch=AM[mi7g][et4m];note_off.velocity=0;if(AM[mi7g][et4m]==ga3m)note_off.send();else{if(MO_ON_OFF==-1)note_off.sendAfterMilliseconds(KS_OFF_time);else{note_off.sendAfterMilliseconds(KS_OFF_time+MS[0])}}}}if(AM[mi7g][et4m_m]>-1&&AM[mi7g][et4m_m]<ga3m){var note_on=new NoteOn;note_on.channel=AM[mi7g][gh4l];note_on.pitch=AM[mi7g][et4m_m];note_on.velocity=KS_ON_Vel;
if(MO_ON_OFF==-1)note_on.sendAfterMilliseconds(KS2_ON_time);else{note_on.sendAfterMilliseconds(MS[0]);}if(AM[mi7g][tv9a]>0){pw5z[(AM[mi7g][gh4l]*ga3m)+AM[mi7g][et4m_m]]=1;}else{var note_off=new NoteOff;note_off.channel=AM[mi7g][gh4l];note_off.pitch=AM[mi7g][et4m_m];note_off.velocity=0;if(AM[mi7g][et4m_m]==ga3m)note_off.send();else{if(MO_ON_OFF==-1)note_off.sendAfterMilliseconds(KS_OFF_time);else{note_off.sendAfterMilliseconds(KS_OFF_time+MS[0])}}}}}function vj3l(){if(AM[mi7g][wt7h]>-1){var Prg=new ProgramChange;
Prg.channel=AM[mi7g][gh4l];Prg.number=AM[mi7g][wt7h]+PC_Offset;if(Prg.number>=0){if(MO_ON_OFF==-1)Prg.send();else{Prg.sendAfterMilliseconds(MS[1])}}}}function bw7l(){if(AM[mi7g][ja3b]>-1){var ControlA=new ControlChange;ControlA.channel=AM[mi7g][gh4l];ControlA.number=AM[mi7g][ja3b];ControlA.value=AM[mi7g][ja3bV]+CCa_Offset;if(ControlA.value>=0){if(MO_ON_OFF==-1)ControlA.send();else{ControlA.sendAfterMilliseconds(MS[2])}}}}function lq3b(){if(AM[mi7g][oa4x]>-1){var ControlB=new ControlChange;
ControlB.channel=AM[mi7g][gh4l];ControlB.number=AM[mi7g][oa4x];ControlB.value=AM[mi7g][oa4xV]+CCb_Offset;if(ControlB.value>=0){if(MO_ON_OFF==-1)ControlB.send();else{ControlB.sendAfterMilliseconds(MS[3])}}}}function sf4h(){if(Link_Plg==1){var fg1j=new ControlChange;fg1j.channel=AM[mi7g][gh4l];fg1j.number=RC_Num;if(et6m==1){fg1j.value=bi2s[uc5d[oa3n]-1];}if(et6m==2){fg1j.value=Math.abs(bi2s2[AM[mi7g][gh4l]-1][0]-mi7g);}fg1j.send();}}function pa3m(){for(i=ga3m;i<ga3m*17;i++){if(pw5z[i]==1&&i>ga3m)
{var note_on=new NoteOn;note_on.channel=Math.floor(i/ga3m);note_on.pitch=i-(ga3m*Math.floor(i/ga3m));note_on.velocity=KS_ON_Vel;if(MO_ON_OFF==-1)note_on.sendAfterMilliseconds(Auto_Latch_time);else{note_on.sendAfterMilliseconds(MS[0]+Auto_Latch_time);}}}}function ParameterChanged(param,value){bi2s[param]=value;for(i=0;i<=3;i++){if(CC_send[i][1]>-1&&pv3k==0){var cc=new ControlChange;for(var k=1;k<=16;k++){if(CC_send[i][0]==0){cc.channel=k;cc.number=CC_send[i][1];cc.value=CC_send[i][2];}else{cc.channel=CC_send[i][0];
cc.number=CC_send[i][1];cc.value=CC_send[i][2];}cc.send();}}}pv3k=1;if(et6m==1){if(param>=0&&param<=15){oa3n=param;mi7g=bi2s2[uc5d[oa3n]-1][bi2s[oa3n]];be6k();}}if(et6m==2||et6m==4){if(STO==1){if(ow8m!=AM[bi2s[0]][gh4l]){ic8f=ow8m;}ow8m=AM[bi2s[0]][gh4l];if(ic8f!=-1){if(AM[bi2s[0]][gh4l]!=ic8f){for(i=0;i<ga3m;i++){ks1f[(eh5k*ga3m)+i]=sw7k[i];kq4b[i]=1;}}}}oa3n=0;mi7g=value;be6k();}}function HandleMIDI(e){if(RC==1){if(e instanceof ControlChange&&e.number==RC_Num){if(et6m==1){for (i=0;i<=15;i++){if(uc5d[i]==e.channel)
{SetParameter(i,e.value+RC_Offset);}}}if(et6m==2||et6m==3){SetParameter(0,e.value+RC_Offset);}if(RC_Thru==-1){return undefined;}}}if(et6m==1||et6m==2){if(e instanceof NoteOn){if(KS_Filter==1){for (i=0;i<=lq8m;i++){if(e.channel==AM[i][gh4l]&&e.pitch==AM[i][et4m]||e.channel==AM[i][gh4l]&&e.pitch==AM[i][et4m_m]){return undefined;}}}if(bw5l==1){if(bi2s[1]==1)le4c[e.pitch]=bi2s[2]+1;else{le4c[e.pitch]=AM[bi2s[0]][gh4l];}}}if(e instanceof ControlChange){if(CC_Filter==1){for(i=0; i<=lq8m;i++){
if(e.channel==AM[i][gh4l]&&e.number==AM[i][ja3b]||e.channel==AM[i][gh4l]&&e.number==AM[i][oa4x]){return undefined;}}}}if(e instanceof ProgramChange){if(PC_Filter==1){for (i=0; i<=lq8m;i++){if(e.channel==AM[i][gh4l]&&e.number==AM[i][wt7h]){return undefined;}}}}if(bw5l==1){if(e instanceof NoteOff)e.channel=le4c[e.pitch];else{if(bi2s[1]==1)e.channel=bi2s[2]+1;else{e.channel=AM[bi2s[0]][gh4l];}}if(e instanceof ControlChange&&STO==1){if(e.channel!=ic8f&&kq4b[e.number]==1){
if(ks1f[(e.channel*ga3m)+e.number]>=0){if(ks1f[(e.channel*ga3m)+e.number]!= e.value)hy0l=0;else{hy0l=1;kq4b[e.number]=0;}}}eh5k=e.channel;sw7k[e.number]=e.value;if(hy0l==0){return undefined;}}}}if(e instanceof NoteOn&&et6m==3){e.articulationID=GetParameter(0)+1;le4c[e.pitch]=e.articulationID;}if(e instanceof NoteOff&&et6m==3){e.articulationID=le4c[e.pitch];}if(et6m==4){for(i=0;i<=lq8m;i++){if(AM[i][gh4l]==e.channel){z=i;i=300;if(e instanceof NoteOn){
if(e.articulationID<rt4f[e.channel]&&df4k[e.channel]==1){SetParameter(0,z+e.articulationID);}if(df4k[e.channel]==0){SetParameter(0,z);}}if(df4k[e.channel]==1){e.sendAfterMilliseconds(25);}else{e.send();}}}}else{e.send();}}

// END CODE""")

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
