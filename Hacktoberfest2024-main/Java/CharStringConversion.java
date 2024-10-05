public class CharStringConversion {
    public static void main(String[] args) {
        // Convert char to String
        char c = 'A';
        String str1 = Character.toString(c);
        String str2 = String.valueOf(c);
        String str3 = "" + c;

        System.out.println("char to String:");
        System.out.println("Original char: " + c);
        System.out.println("Using Character.toString(): " + str1);
        System.out.println("Using String.valueOf(): " + str2);
        System.out.println("Using concatenation: " + str3);

        // Convert String to char
        String s = "Hello";
        char firstChar = s.charAt(0);
        char[] charArray = s.toCharArray();

        System.out.println("\nString to char:");
        System.out.println("Original String: " + s);
        System.out.println("First character: " + firstChar);
        System.out.print("All characters: ");
        for (char ch : charArray) {
            System.out.print(ch + " ");
        }
    }
}