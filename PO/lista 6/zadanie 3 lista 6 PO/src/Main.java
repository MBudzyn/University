/*
Mateusz Budzyński
zadanie 1 oraz 3 testy w jednym pliku main
 */






import java.io.*;

public class Main {

    private static final Bufor<String> bufor = new Bufor<>(1000);


    public static void main(String[] args) {


        int licznik = bufor.rozmiar();
        Thread producer = new Thread(() -> {
            for (int i = 0; i < licznik; i++) {

                synchronized (bufor) {
                    while (bufor.jestpelny()) {
                        try {
                            bufor.wait();
                        } catch (InterruptedException e) {
                            throw new RuntimeException(e);
                        }
                    }
                    bufor.add("Item no. " + i);
                    System.out.println("producer made item :" + i);
                    bufor.notify();

                }
            }

        });

        Thread consumer = new Thread(() -> {
            int pozostaleele= licznik;
            while (pozostaleele > 0) {
                String item;
                synchronized (bufor) {
                    while (bufor.jestpusty()) {
                        try {
                            bufor.wait();
                        } catch (InterruptedException e) {
                            throw new RuntimeException(e);
                        }
                    }
                    item = bufor.zwroc();
                }
                pozostaleele--;
                System.out.println("Consumer got item: " + item);

            }
        });

        producer.start();
        consumer.start();



        try {

            FileOutputStream plikwyjsciowy = new FileOutputStream("mojaKolekcja.ser");
            ObjectOutputStream wyjscie = new ObjectOutputStream(plikwyjsciowy);
            wyjscie.writeObject(bufor);
            wyjscie.close();
            plikwyjsciowy.close();
            System.out.println("Kolekcja została zapisana na dysku");

        } catch (IOException ex) {
            ex.printStackTrace();
        }

        Bufor<String> zmiennabufor;
        try {
            FileInputStream plikwejsciowy = new FileInputStream("mojaKolekcja.ser");
            ObjectInputStream wejscie = new ObjectInputStream(plikwejsciowy);
            zmiennabufor = (Bufor<String>) wejscie.readObject();
            wejscie.close();
            plikwejsciowy.close();
            System.out.println("Kolekcja została wczytana z dysku:");
            System.out.println(zmiennabufor);
        }
        catch (IOException ex)
        {
            ex.printStackTrace();
        }
        catch (ClassNotFoundException e)
        {
            e.printStackTrace();
        }

    }

    }

