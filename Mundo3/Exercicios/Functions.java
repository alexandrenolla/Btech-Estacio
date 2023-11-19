public class Functions {
    public static void main(String[] args) {
        String nomeInput = "Alexandre";
        saudacao(nomeInput);

        System.out.println(sum(2,3));
        
    }

    public static void saudacao(String nomeParametro) {
        System.out.println("Hello " + nomeParametro);
    }

    public static int sum(int a, int b) {
        return a + b;
    }
}
