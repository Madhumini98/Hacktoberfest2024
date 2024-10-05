public class AverageCalculator {
    public static void main(String[] args) {
        // Sample array of numbers
        int[] numbers = { 5, 10, 15, 20, 25 };

        // Calculate the sum
        int sum = 0;
        for (int number : numbers) {
            sum += number;
        }

        // Calculate the average
        double average = (double) sum / numbers.length;

        // Print the result
        System.out.println("The average is: " + average);
    }
}