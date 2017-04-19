#include <iostream>
#include <ardcom/ardcom.h>
#include <ardcom/ardcomoutshm.h>
#include <ardcom/ardcominshm.h>

#include <yarp/os/Bottle.h>
#include <yarp/os/Property.h>
#include <yarp/os/BufferedPort.h>
#include <yarp/os/Network.h>
#include <yarp/os/Time.h>

#include <stdio.h>

ArdComOut* comout = 0;
ArdComIn* comin = 0;
float enable_com[250] = {2,3,5};

struct Ard_Out_Packet{
    float Con_Mod;
    float Enable[5];
    float Pos_Com[15];
    float Stiffness[15];
    float Damping[15];
    float Velocity[15];
    float Kp[15];
    float Con_Mod1;
    float Enable1[5];
    float Pos_Com1[15];
    float Stiffness1[15];
    float Damping1[15];
    float Velocity1[15];
    float Kp1[15];
    float emergency;
    float Reserved[87];
};

Ard_Out_Packet out_packet;

struct Ard_Input_Packet{
    float Pos[15];
    float Torque[15];
    float Velocity[15];
    float Enabled[5];
    float brakestatus;
    float handconfig[2];
    float commstatus;
    float Pos1[15];
    float Torque1[15];
    float Velocity1[15];
    float Enabled1[5];
    float Reserved[146];
};

Ard_Input_Packet in_packet;

float input_packet[250];
int input_packet_size = 250;
//float buf[250];


void send_package(){
    int ret;
    ArdComInShm* ret2;
    fprintf(stderr, "Send package\n");
    if( comout == 0 || (ArdComOutShm*)comout -> send((void *)&out_packet, sizeof(Ard_Out_Packet)) <= 0){
        fprintf(stderr,"ardcomoutudp::send() failed\n");
        }
    //else{fprintf(stderr,"ardcomoutudp::send() success\n");}

    ret2 = (ArdComInShm*)comin->tryrec((void *)&in_packet, sizeof(Ard_Input_Packet));

    fprintf(stderr, "Package sent\n");

    //ret = (int)(ArdComInShm*)comin->rec((void *)&in_packet, sizeof(Ard_Input_Packet));
    if(ret2 == 0){
        fprintf(stderr,"ardcominudp::no new data!\n");
        return; // no new data
        }
    else {
        ret = comin->rec((void *)&in_packet, sizeof(Ard_Input_Packet));
        if(comin == 0 || ret < 0) {
            fprintf(stderr,"ardcominudp::rec() failed\n");
            return;
        }

    fprintf(stderr,"ardcomoutudp::send() 5\n");

    }


    //QString test = QString::number(in_packet.Pos[0],'g',6);
    for(int j = 0; j<15; j++){
    fprintf(stderr, "%f\n", in_packet.Pos[j]);
    }

    //port 1 enabled
    float en_1 = in_packet.Enabled[0];

    float en_2 = in_packet.Enabled[1];

    float en_3 = in_packet.Enabled[2];

    float en_4 = in_packet.Enabled[3];

    float en_5 = in_packet.Enabled[4];

    //port 2 enabled
    float en_11 = in_packet.Enabled1[0];

    float en_21 = in_packet.Enabled1[1];

    float en_31 = in_packet.Enabled1[2];

    float en_41 = in_packet.Enabled1[3];

    float en_51 = in_packet.Enabled1[4];

    //emergency stop status
    float stop = in_packet.brakestatus;

    //hand config
    float handconfig1 = in_packet.handconfig[0];

    float handconfig2 = in_packet.handconfig[1];

    //communication status
    float status = in_packet.commstatus;

    //only for debug
    out_packet.Kp[0]=5;
    out_packet.Kp[1]=5;
    out_packet.Kp[2]=5;
    out_packet.Kp[3]=5;
    out_packet.Kp[4]=5;
    out_packet.Kp[5]=5;
    out_packet.Kp[6]=5;
    out_packet.Kp[7]=5;
    out_packet.Kp[8]=5;
    out_packet.Kp[9]=5;
    out_packet.Kp[10]=5;
    out_packet.Kp[11]=5;
    out_packet.Kp[12]=5;
    out_packet.Kp[13]=5;
    out_packet.Kp[14]=5;
    //only for debug
    out_packet.Kp1[0]=5;
    out_packet.Kp1[1]=5;
    out_packet.Kp1[2]=5;
    out_packet.Kp1[3]=5;
    out_packet.Kp1[4]=5;
    out_packet.Kp1[5]=5;
    out_packet.Kp1[6]=5;
    out_packet.Kp1[7]=5;
    out_packet.Kp1[8]=5;
    out_packet.Kp1[9]=5;
    out_packet.Kp1[10]=5;
    out_packet.Kp1[11]=5;
    out_packet.Kp1[12]=5;
    out_packet.Kp1[13]=5;
    out_packet.Kp1[14]=5;
    //only for debug
    out_packet.Stiffness[0]=0.023;
    out_packet.Stiffness[1]=0.023;
    out_packet.Stiffness[2]=0.023;
    out_packet.Stiffness[3]=0.023;
    out_packet.Stiffness[4]=0.023;
    out_packet.Stiffness[5]=0.023;
    out_packet.Stiffness[6]=0.023;
    out_packet.Stiffness[7]=0.023;
    out_packet.Stiffness[8]=0.023;
    out_packet.Stiffness[9]=0.023;
    out_packet.Stiffness[10]=0.023;
    out_packet.Stiffness[11]=0.023;
    out_packet.Stiffness[12]=0.023;
    out_packet.Stiffness[13]=0.023;
    out_packet.Stiffness[14]=0.023;
    //only for debug
    out_packet.Stiffness1[0]=0.023;
    out_packet.Stiffness1[1]=0.023;
    out_packet.Stiffness1[2]=0.023;
    out_packet.Stiffness1[3]=0.023;
    out_packet.Stiffness1[4]=0.023;
    out_packet.Stiffness1[5]=0.023;
    out_packet.Stiffness1[6]=0.023;
    out_packet.Stiffness1[7]=0.023;
    out_packet.Stiffness1[8]=0.023;
    out_packet.Stiffness1[9]=0.023;
    out_packet.Stiffness1[10]=0.023;
    out_packet.Stiffness1[11]=0.023;
    out_packet.Stiffness1[12]=0.023;
    out_packet.Stiffness1[13]=0.023;
    out_packet.Stiffness1[14]=0.023;
    //olny for debug
    out_packet.Velocity[0]=120;
    out_packet.Velocity[1]=120;
    out_packet.Velocity[2]=120;
    out_packet.Velocity[3]=120;
    out_packet.Velocity[4]=120;
    out_packet.Velocity[5]=120;
    out_packet.Velocity[6]=120;
    out_packet.Velocity[7]=120;
    out_packet.Velocity[8]=120;
    out_packet.Velocity[9]=120;
    out_packet.Velocity[10]=120;
    out_packet.Velocity[11]=120;
    out_packet.Velocity[12]=120;
    out_packet.Velocity[13]=120;
    out_packet.Velocity[14]=120;
    //olny for debug
    out_packet.Velocity1[0]=120;
    out_packet.Velocity1[1]=120;
    out_packet.Velocity1[2]=120;
    out_packet.Velocity1[3]=120;
    out_packet.Velocity1[4]=120;
    out_packet.Velocity1[5]=120;
    out_packet.Velocity1[6]=120;
    out_packet.Velocity1[7]=120;
    out_packet.Velocity1[8]=120;
    out_packet.Velocity1[9]=120;
    out_packet.Velocity1[10]=120;
    out_packet.Velocity1[11]=120;
    out_packet.Velocity1[12]=120;
    out_packet.Velocity1[13]=120;
    out_packet.Velocity1[14]=120;

}

using namespace yarp::os;

void yarp_idling(BufferedPort<Bottle> *in, BufferedPort<Bottle> *out) {
  while(1) {
    printf("Cycling\n");
    Bottle *inbottle=in->read(false);
    if(inbottle!=NULL) {
      printf("Bottle %s\n", inbottle->toString().c_str());
      int j=0;
      //Con Mod
      out_packet.Con_Mod=inbottle->get(j++).asDouble();
      //Enable
      for(int i=0; i<5; i++){
        out_packet.Enable[i]=inbottle->get(j++).asDouble();
      }
      //Pos_Com
      for(int i=0; i<15; i++){
        out_packet.Pos_Com[i]=inbottle->get(j++).asDouble();
      }
      //Stiffness
      for(int i=0; i<15; i++){
        out_packet.Stiffness[i]=inbottle->get(j++).asDouble();
      }
      //Damping
      for(int i=0; i<15; i++){
        out_packet.Damping[i]=inbottle->get(j++).asDouble();
      }
      //Velocity
      for(int i=0; i<15; i++){
        out_packet.Velocity[i]=inbottle->get(j++).asDouble();
      }
      //Kp
      for(int i=0; i<15; i++){
        out_packet.Kp[i]=inbottle->get(j++).asDouble();
      }
      //Con Mod1
      out_packet.Con_Mod1=inbottle->get(j++).asDouble();
      //Enable1
      for(int i=0; i<5; i++){
        out_packet.Enable1[i]=inbottle->get(j++).asDouble();
      }
      //Pos_Com1
      for(int i=0; i<15; i++){
        out_packet.Pos_Com1[i]=inbottle->get(j++).asDouble();
      }
      //Stiffness1
      for(int i=0; i<15; i++){
        out_packet.Stiffness1[i]=inbottle->get(j++).asDouble();
      }
      //Damping1
      for(int i=0; i<15; i++){
        out_packet.Damping1[i]=inbottle->get(j++).asDouble();
      }
      //Velocity1
      for(int i=0; i<15; i++){
        out_packet.Velocity1[i]=inbottle->get(j++).asDouble();
      }
      //Kp1
      for(int i=0; i<15; i++){
        out_packet.Kp1[i]=inbottle->get(j++).asDouble();
      }
      out_packet.emergency=inbottle->get(j++).asDouble();
    }
    Bottle& outbottle=out->prepare();
    outbottle.clear();
    //pos
    for(int i=0; i<15; i++) {
      outbottle.addDouble(in_packet.Pos[i]);
    }
    //torque
    for(int i=0; i<15; i++) {
      outbottle.addDouble(in_packet.Torque[i]);
    }
    //Velocity
    for(int i=0; i<15; i++) {
      outbottle.addDouble(in_packet.Velocity[i]);
    }
    //Enabled
    for(int i=0; i<5; i++) {
      outbottle.addDouble(in_packet.Enabled[i]);
    }
    //brakestatus
    outbottle.addDouble(in_packet.brakestatus);
    //handconfig
    for(int i=0; i<2; i++) {
      outbottle.addDouble(in_packet.handconfig[i]);
    }
    //commstatus
    outbottle.addDouble(in_packet.commstatus);
    //Pos1
    for(int i=0; i<15; i++) {
      outbottle.addDouble(in_packet.Pos1[i]);
    }
    //Torque1
    for(int i=0; i<15; i++) {
      outbottle.addDouble(in_packet.Torque1[i]);
    }
    //Velocity1
    for(int i=0; i<15; i++) {
      outbottle.addDouble(in_packet.Velocity1[i]);
    }
    //Enabled1
    for(int i=0; i<15; i++) {
      outbottle.addDouble(in_packet.Enabled1[i]);
    }

    out->writeStrict();
    Time::delay(0.01);
    send_package();
  }
}

void yarp_init() {
  Network yarp;
  ContactStyle style;
  style.persistent=true;
  BufferedPort<Bottle> in;
  BufferedPort<Bottle> out;
  in.setStrict();
  in.open("/hand/in");
  out.open("/hand/out");
  Network::connect("/hand/out", "/read", style);
  Network::connect("/write", "/hand/in", style);
  yarp_idling(&in, &out);
  
}

int main() {
  std::cout<<"Hello World"<<std::endl;
  char* output_shm_name = "gui_out";
  char* input_shm_name = "gui_in";

 /*----------------------Linux ArdNet initiate----------------------------------------------------------------------------------------------------*/
 /*----------------------Linux Sharememory initiate----------------------------------------------------------------------------------------------------*/
    comout = new ArdComOutShm(output_shm_name, false);
    if(!comout){
        fprintf(stderr, "could not create shm gui_out!\n");
    }
    if((ArdComOutShm*)comout->init(sizeof(Ard_Out_Packet)) < 0){
        fprintf(stderr, "could not init shm gui_out!\n");
        delete comout;
        comout = NULL;
    }

    fprintf(stderr, "ardoshm initiation done!\n");
    fprintf(stderr, "now trying to initiate ardishm!\n");

    comin = new ArdComInShm(input_shm_name, false);
    if(!comin){
        fprintf(stderr, "could not create shm gui_in!\n");
    }
    if((ArdComInShm*)comin->init(sizeof(Ard_Input_Packet)) < 0){
        fprintf(stderr, "could not init shm gui_in!\n");
        delete comin;
        comin = NULL;
    }
    fprintf(stderr, "ardishm initiation done!\n");
/*----------------------Linux Sharememory initiate----------------------------------------------------------------------------------------------------*/

/*-------------------------------------QNX ArdNet initiate----------------------------------------------------------------------------------------*/
    send_package();
    yarp_init();

}
