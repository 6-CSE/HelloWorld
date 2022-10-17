public class HelloWorld2 {
	public static void main(String[] args) {
        int[] asciiArray = {72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100};
        for(int i : asciiArray) {
            System.out.print((char)i);
        }
        System.out.println();
	}
}