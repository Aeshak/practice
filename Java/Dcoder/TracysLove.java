import java.util.*;


/*Please dont change class name, Dcoder 
 and class must not be public*/

//Compiler version JDK 1.8


class Dcoder
{ 
	public static void main(String args[])
	{
		int a,b;
		Scanner scn = new Scanner(System.in);
		a = scn.nextInt();
		b = scn.nextInt();
		if (Math.abs(a-b) == 6 || Math.abs(a+b) == 6) {
			System.out.println("Love");
		}
		else {
			System.out.println("Hate");
		}
	}
}
