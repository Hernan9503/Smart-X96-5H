CC = gcc
#CFLAGS  = -O2 -Wall -g -I/usr/local/include/modbus
CFLAGS  = -O2 -Wall -g `pkg-config --cflags libmodbus`
#LDFLAGS = -O2 -Wall -g -L/usr/local/lib -lmodbus
LDFLAGS = -O2 -Wall -g `pkg-config --libs libmodbus`

#SDM = sdm120c
SMARTX96 = SmartX96-5H
%.o: %.py
	$(CC) -c -o $@ $< $(CFLAGS)

${SMARTX96}: SmartX96-5H.o 
	$(CC) -o $@ SmartX96-5H.o $(LDFLAGS)
	chmod 4711 ${SMARTX96}

strip:
	strip ${SMARTX96}

clean:
	rm -f *.o ${SMARTX96}

install: ${SMARTX96}
	install -m 4711 $(SMARTX96) /usr/local/bin

uninstall:
	rm -f /usr/local/bin/$(SMARTX96)
