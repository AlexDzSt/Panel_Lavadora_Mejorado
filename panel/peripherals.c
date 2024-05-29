#include <stdio.h>
#include "pico/stdlib.h"
#include "hardware/gpio.h"

void init_led(int pin){
    gpio_init(pin);
    gpio_set_dir(pin, GPIO_OUT);
}

void encender_led(int pin){
    gpio_put(pin, !gpio_get(pin));
}

void apagar_led(int pin){
    gpio_put(pin, 0);
}

void init_boton(int pin){
    gpio_init(pin);
    gpio_set_dir(pin, GPIO_IN);
    gpio_set_pulls(pin, true, false);
}

bool leer_boton_OnOff(int boton_OnOff, int led_OnOff){
    bool boton_OnOff_presionado = false;

    if (!gpio_get(boton_OnOff) && !boton_OnOff_presionado)
    {
        encender_led(led_OnOff);
        boton_OnOff_presionado = true;
    }else if (gpio_get(boton_OnOff) && boton_OnOff_presionado)
    {
        boton_OnOff_presionado = false;
    }
}

void init_display(int primer_gpio){
    for(int gpio = primer_gpio; gpio < primer_gpio + 14; gpio++){
        gpio_init(gpio);
        gpio_set_dir(gpio, GPIO_OUT);
    }
}

void turn_display_on(int bits[], int val, int primer_gpio){
    int32_t mask = bits[val / 10] << (primer_gpio + 7); // Máscara para el primer display
    gpio_set_mask(mask);
    int32_t mask2 = bits[val % 10] << primer_gpio; // Máscara para el segundo display
    gpio_set_mask(mask2);
}

void clear_display(int bits[], int val, int primer_gpio){
    int32_t mask = bits[val / 10] << (primer_gpio + 7); // Máscara para el primer display
    int32_t mask2 = bits[val % 10] << primer_gpio; // Máscara para el segundo display
    gpio_clr_mask(mask | mask2);
}