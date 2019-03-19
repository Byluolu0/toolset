#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <errno.h>
#include <unistd.h>
#include <string.h>

#include <iostream>

int connectTo(const char* testhost, unsigned short testport)
{
    int sock = socket(AF_INET, SOCK_STREAM, 0);
    if(sock < 0)
    {
        std::cout << "get socket failed: " <<  strerror(errno) << std::endl;
        return -1;
    }

    struct sockaddr_in testaddr;

    memset((void *)&testaddr, 0, sizeof(testaddr));
    testaddr.sin_family = AF_INET;
    testaddr.sin_port = htons(testport);

    if(inet_aton(testhost, &testaddr.sin_addr) < 0)
    {
        close(sock);
        return -1;
    }

    int rtcode = connect(sock, (struct sockaddr *)&testaddr, sizeof(testaddr));
    if(rtcode < 0)
    {
        std::cout << "connect to failed " << testhost << " " << testport << " " << errno << " " << strerror(errno) << std::endl;
        close(sock);
        return -1;
    }

    std::cout << "connect success" << sock;

    return sock;
}

int main()
{
    int ret = connectTo("23.105.218.162", 26508);
}