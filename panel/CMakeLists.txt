add_executable(panel
                led.c
                main_panel.c
        )     

# pull in common dependencies
target_link_libraries(panel pico_stdlib hardware_gpio hardware_timer hardware_uart hardware_adc)

# enable usb output, disable uart output
pico_enable_stdio_usb(panel 1)
pico_enable_stdio_uart(panel 1)

# create map/bin/hex file etc.
pico_add_extra_outputs(panel)

