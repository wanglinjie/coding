#ifndef __MY_HEAD__
#define __MY_HEAD__
#include <pcap.h>

// ���а��������������, ������
class Head_Super{
public:
	// ָ����߲�Э��
	Head_Super* next;

	// �� pkt_data �г�ȡ�����Э��PDU����Ϣ
	virtual void analysis(u_char *pkt_data)=0;

	// �����Э�����ϸ��Ϣ��һ���ַ������ֳ���
	virtual CString my_print()=0;
};

class Head_Ethernet : public Head_Super{
public:
	u_char S_Mac[6];
	u_char D_Mac[6];
	u_char kind[2];   //0800:IP  0806:ARP
	void analysis(u_char *pkt_data);
	CString my_print();
};

class Head_802_3 : public Head_Super{
public:
	u_char S_Mac[6];
	u_char D_Mac[6];
	u_char kind[2];   //0800:IP  0806:ARP
	void analysis(u_char *pkt_data);
	CString my_print();
};

class Head_ARP : public Head_Super{
public:
	u_char op[2];  //require or answer
	u_char S_Mac[6];
	u_char S_IP[4];
	u_char D_Mac[6];
	u_char D_IP[4];
	void analysis(u_char *pkt_data);
	CString my_print();
};

class Head_IP : public Head_Super{
public:
	int version;	//����ȡIP�ײ���һ���ֽڣ�ֻ��ȡǰ4λ
	int len;		//ȡ��������4λ
	u_char sign[2];	//��ʶ��
	u_char TTL;		//���ʱ��
	int protocol;
	u_char S_IP[4];
	u_char D_IP[4];
	void analysis(u_char *pkt_data);
	CString my_print();
};

class Head_ICMP : public Head_Super{
public:
	int kind;
	int code;
	void analysis(u_char *pkt_data);
	CString my_print();
};

class Head_UDP : public Head_Super{
public:
	u_char S_Port[2];
	u_char D_Port[2];
	void analysis(u_char *pkt_data);
	CString my_print();
};

class Head_IGMP : public Head_Super{
public:
	int version; // should be 3
	u_char type;
	u_char Multicast[4];
	void analysis(u_char *pkt_data);
	CString my_print();
};

class Head_TCP : public Head_Super{
public:
	u_char S_Port[2];
	u_char D_Port[2];
	u_char SYN[4];
	u_char ACK[4];
	u_char Size_Window[2];
	int len;
	void analysis(u_char *pkt_data);
	CString my_print();
};

class Head_IPv6 : public Head_Super{
public:
	int version;
	int protocol;
	int extern_len;
	int sign;						//���ڱ���Ƿ�����չ�ײ�
	u_char S_IPv6[16];
	u_char D_IPv6[16];
	void analysis(u_char *pkt_data);
	CString my_print();
};

class Head_OSPF : public Head_Super{
public:
	int version;
	int type;
	u_char Router_ID[4];
	u_char Area_ID[4];
	void analysis(u_char *pkt_data);
	CString my_print();
};

class Head_DNS : public Head_Super{
public:
	u_char ID[2];
	int Question;
	void analysis(u_char *pkt_data);
	CString my_print();
};

class Head_HTTP : public Head_Super{
public:
	void analysis(u_char *pkt_data);
	CString my_print();
};

class Head_FTP : public Head_Super{
public:
	void analysis(u_char *pkt_data);
	CString my_print();
};
#endif