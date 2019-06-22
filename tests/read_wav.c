#include <stdio.h>
#include <stdlib.h>
#include <string.h>



int main(int argc,char *argv[])
{
	FILE *fd;
	//char buffer[4];
	char *buffer;
	buffer = (char *)malloc(4);

	fd = fopen("Angele-Balancetonquoi.wav", "r");
    printf("%s\n", strerror(errno));

	fread(buffer,4, 1, fd);
	fclose(fd);

	printf("%c%c%c%c", buffer[0], buffer[1], buffer[2], buffer[3]);

	
}