/*
 * This is sample code generated by rpcgen.
 * These are only templates and you can use them
 * as a guideline for developing your own functions.
 */

#include "media.h"


void
add_prog_5(char *host)
{
	CLIENT *clnt;
	int  *result_1;
	numbers  add_5_arg;

#ifndef	DEBUG
	clnt = clnt_create (host, ADD_PROG, ADD_VERS, "udp");
	if (clnt == NULL) {
		clnt_pcreateerror (host);
		exit (1);
	}
#endif	/* DEBUG */
	
	printf("Digite a nota do primeiro bimestre:\n");
	scanf("%d", &add_5_arg.nota1);
	
	printf("Digite a nota do segundo bimestre:\n");
	scanf("%d", &add_5_arg.nota2);
	
	result_1 = add_5(&add_5_arg, clnt);
	if (result_1 == (int *) NULL) {
		clnt_perror (clnt, "call failed");
	}
	else{
		printf("Media: %d\n",*result_1);
	}
#ifndef	DEBUG
	clnt_destroy (clnt);
#endif	 /* DEBUG */
}


int
main (int argc, char *argv[])
{
	char *host;

	if (argc < 2) {
		printf ("usage: %s server_host\n", argv[0]);
		exit (1);
	}
	host = argv[1];
	add_prog_5 (host);
exit (0);
}