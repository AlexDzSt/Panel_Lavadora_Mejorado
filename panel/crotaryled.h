#ifndef C_ROTARY_LED_H
#define C_ROTARY_LED_H

#include <stdint.h>
#include <stdbool.h>

#define PINS_SIZE 7

/** @brief Digital pins needed to control the rotary led. Indices from zero to six corresponds to led pins A,B,C,D,E,F,G*/
static uint32_t pins[PINS_SIZE];

/** @brief The value indicating the leds to be turned on*/
static uint32_t rl_mask;

/** @brief The time the rotary led delays the reading of the input*/
static uint32_t const rl_delay = 50;

/** @brief Initializes the pins to the rotary led uses*/
void rl_construct(const int a[]);

/** @brief Initiaizes the pins the rotary led uses*/
void rl_init();

/** @brief Turns a led on depending on the read analog value*/
void rl_turn_led_on();

/** @brief Reads the analog value from the output of a potentiometer*/
uint32_t rl_read_value();

/** @brief Clears the seven segment display*/
void rl_clear();

/** @brief Reads the value from the rotary switch, handles the read value, and controls the LED*/
void rotary_led();

/** @brief Handles the value read from the rotary switch and sends the corresponding message via UART*/
//void handle_rotary_value(u_int32_t val);

#endif