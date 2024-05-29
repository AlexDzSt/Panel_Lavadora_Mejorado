#ifndef C_PERIPHERALS_H
#define C_PERIPHERALS_H

/** @brief Inicializa un led dado un GPIO*/
void init_led(int pin);

/** @brief Envia el estado del led negado al GPIO*/
void encender_led(int pin);

/** @brief Envia un 0 al GPIO del led*/
void apagar_led(int pin);

/** @brief Inicializa un boton, dado un numero de GPIO*/
void init_boton(int pin);

/** @brief Si el boton de encendido es presionado se prende el sistema, si vuelve a ser presionado se apaga el sistema*/
bool leer_boton_OnOff(int boton_OnOff, int led_OnOff);

/** @brief Inicializa los GPIOs necesarios para los 2 displays de 7 segmentos*/
void init_display(int primer_gpio);

/** @brief Muestra la cuenta regresiva del temporizador*/
void turn_display_on(int bits[], int val, int primer_gpio);

/** @brief Apaga los leds de los displays de 7 segmentos*/
void clear_display(int bits[], int val, int primer_gpio);

#endif