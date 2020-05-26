semaphore S=l;
semaphore empty=N, apple=0, orange=0;
void Father()
{
	while(1)
	{
		P(empty);
		P(S);
		放水果到盘子里;
		V(S);
		if (放进去的是橘子)
		{
			V(orange);
			放一个橘子; 
		} 
		else
		{
			V(apple)
			放一个苹果; 
		}
		
	} 
}
void Son()
{
	while(1)
	{
		P(apple);
		P(S);
		拿一个苹果;
		V(S);
		V(empty);
		吃一个苹果; 
	}
}
void Daughter()
{
	while(1)
	{
		P(orange);
		P(S);
		拿一个橘子;
		V(S);
		V(orange);
		吃一个橘子; 
	}
}
