/*
manchester.h
Author: Praneet Kapoor
Date:
Description: This header files is to be included in the main code from where the interfacing with the Rx-Tx modules is done. 
The purpose of this library is to encode the serially received data using Manchester coding and transmit it using 433 MHz Tx module. Also included is the capability to decode the data being received from the 433MHz Rx module, decode it, store it and send it to the computer serially.
*/

#ifndef manchester_h
#define manchester_h

#include "Arduino.h"

struct message
{
	uint8_t buffer[64], encoded[128];
	uint8_t start = 0b11110000;
	uint8_t stop = 0b11000011;
	uint8_t 
	uint8_t length;
	uint8_t checksum; //if buffer has N odd bytes, then checksum = N;
};

int clicks(int);			//returns whether the given no. of ticks passed as an argumnet has happened or not.
int encoder();
int decoder();
int send();
int receive(); 

#endif