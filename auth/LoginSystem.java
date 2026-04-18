import java.io.*;
import java.security.MessageDigest;
import java.time.LocalTime;
import java.util.Scanner;

public class LoginSystem {

    public static String hashPassword(String password) throws Exception {
        MessageDigest md = MessageDigest.getInstance("SHA-256");
        byte[] hash = md.digest(password.getBytes());
        StringBuilder hex = new StringBuilder();
        for (byte b : hash) hex.append(String.format("%02x", b));
        return hex.toString();
    }

    public static boolean checkLogin(String username, String password) throws Exception {
        File file = new File("../data/users.txt");

        if (!file.exists()) return false;

        try (BufferedReader br = new BufferedReader(new FileReader(file))) {

            String line;
            String inputHash = hashPassword(password);

            while ((line = br.readLine()) != null) {
                String[] parts = line.split(",");

                if (parts[0].equals(username) && parts[1].equals(inputHash)) {
                    return true;
                }
            }
        }

        return false;
    }

    public static void main(String[] args) throws Exception {

        System.out.println("Cyber SentinelX – Adaptive Threat Monitoring Platform");
        System.out.println("Authentication Module\n");

        // 🔥 TRY-WITH-RESOURCES (fix scanner warning)
        try (Scanner sc = new Scanner(System.in)) {

            System.out.print("Username: ");
            String user = sc.nextLine();

            System.out.print("Password: ");
            String pass = sc.nextLine();

            boolean success = checkLogin(user, pass);

            try (
                FileWriter log = new FileWriter("../data/login_log.txt", true);
                FileWriter failed = new FileWriter("../data/failed_log.txt", true);
                FileWriter live = new FileWriter("../data/live_activity.txt", true)
            ) {

                if (success) {
                    System.out.println("Login successful");
                    log.write(user + "," + LocalTime.now() + "\n");

                    live.write("LOGIN SUCCESS: " + user + " at " + LocalTime.now() + "\n");

                } else {
                    System.out.println("Login failed");
                    failed.write(user + "," + LocalTime.now() + "\n");

                    live.write("FAILED LOGIN: " + user + " at " + LocalTime.now() + "\n");
                }
            }
        }

        // 🔥 Trigger Python SOC
        ProcessBuilder pb = new ProcessBuilder("python", "../core/soc_detector.py");
        pb.inheritIO();
        pb.start();
    }
}