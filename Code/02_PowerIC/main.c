/*
 * SmecarApp.c
 *
 * Created: 29.12.2018. 16.47.40
 * Author : User23
 */ 
#define F_CPU 1200000UL
#include <util/delay.h>
#include <avr/io.h>
#include "stdbool.h"


typedef union _PINB_ {
    uint8_t registerValue;
    struct {
        uint8_t PINB0_Value:1;
        uint8_t PINB1_Value:1;
        uint8_t PINB2_Value:1;
        uint8_t PINB3_Value:1;  // KL15 R1 PB3
        uint8_t PINB4_Value:1;  // KL30 R2 PB4
        uint8_t PINB5_Value:1; 
        uint8_t Reserved:2;  
         };
} PINB_t;

 PINB_t* pinb;
void Init();
void PowerController();
int main(void)
{
	Init();
        while (1) 
    {
		PowerController();//proverava na kojim su pinovima signali prisutni i na osnovu njih radi dalje.
	}
}
void Init()
{
    pinb =(PINB_t*)&(*(volatile uint8_t *)(0x36));
  	
    PORTB |= (1<<PORTB0) /*| (1<<PORTB1) | (1<<PORTB2) */| (1<<PORTB3) | (1<<PORTB4) ;//PINOVI 3 I 5 PORTA B SU INPUT I AKTIVIRAN IM JE PULLUP OTPORNIK pin 1 i 2 output]
  	DDRB |= (1<<DDB1) | (1<<DDB2);//PINOVI 2 I 1 PORTA B SU OUTPUT
    PORTB |= 1<<PORTB1; //KL30  HIGH - OFF
    _delay_ms(10U);
  }
void PowerController()
{
    static bool l_FirstStart = true;
    
    
   if ( (false == pinb->PINB4_Value)  && (false == pinb->PINB3_Value) )
	{
	   PORTB &= ~(1<<PORTB1); // KL30 output  PIN1 connector inverse P type FET LOW - ON
        if(true == l_FirstStart)
        {
           _delay_ms(500U);
           l_FirstStart = false;
        }
        PORTB |= 1<<PORTB2; // KL15 output  PIN1 connector
    }

	
    if( (false == pinb->PINB4_Value) &&  (true == pinb->PINB3_Value) && (false == l_FirstStart) ) 
    {
        PORTB &= ~(1<<PORTB2); // KL15 LOW
        _delay_ms(2000U);
        PORTB |= 1<<PORTB1; //KL30  HIGH - OFF
    }
    
    if((true == pinb->PINB4_Value)  && (true == pinb->PINB3_Value))
    {
        PORTB &= ~(1<<PORTB2); // KL15 LOW
        _delay_ms(2000U);
        PORTB |= 1<<PORTB1; //KL30  HIGH - OFF
    }
   _delay_ms(10U);
}



