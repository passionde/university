#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include <string.h>
#include <alsa/asoundlib.h>



int main()
{
    int fd;
    char msg[1024] = "10";

    fd = open("/dev/password_gen", O_RDWR);

    if (fd < 0) {
        perror("Failed to open the device...");
        return 1;
    }

    read(fd, msg, sizeof(msg));
    printf("Read from device: %s\n", msg);
    close(fd);
}