public class Arrays {
    public static void main(String[] args) {

        // int[] numeros = new int[5];
        int[] numeros = {9, 10, 12, 25, 2};
        // numeros[0] = 1;
        // numeros[1] = 2;
        // numeros[2] = 3;
        // numeros[3] = 4;
        // numeros[4] = 5;
        int maior = numeros[0];
        int menor = numeros[0];
        int media = 0;

        for (int i=0; i < numeros.length; i++) {
            if (numeros[i] > maior) {
                maior = numeros[i];
            }
            if (numeros[i] < menor) {
                menor = numeros[i];
            }
            media += numeros[i];
        }
        System.out.println("Maior: " + maior);
        System.out.println("Menor: " + menor);
        System.out.println("Media: " + media/numeros.length);

        
        String[] letras = { "a", "b", "c" };

        for (int i=0; i < letras.length; i++) {
            System.out.println(letras[i]);
        }

    }
}