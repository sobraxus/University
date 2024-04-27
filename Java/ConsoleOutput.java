package IOT_System;

import java.util.Scanner;

public class ConsoleOutput {
    public void consoleOutput(String data) {
        System.out.println(data);
    }

    public int getInt(String gInt) { //Method to get user inputted integer from console
        Scanner input = new Scanner(System.in);
        consoleOutput(gInt);
        return input.nextInt();
    }

    public String getString(String gString) {  //Method to get user inputted String from console
        Scanner input = new Scanner(System.in);
        consoleOutput(gString);
        return input.next();
        /* PRINTS TO CONSOLES */
    }

    public void prntString(String str) { //Prints String data to console
        Shortcuts sCuts = new Shortcuts();
        sCuts.printString(str);
    }

    public void prntInt(int Int) { //Prints Integer data to console
        Shortcuts sCuts = new Shortcuts();
        sCuts.printInteger(Int);
    }

    public void prntDouble(int Dbl) { //Prints Double data to console
        Shortcuts sCuts = new Shortcuts();
        sCuts.printDouble(Dbl);
    }

    public void prntFloat(float flt) {//Prints Float data to console
        Shortcuts sCuts = new Shortcuts();
        sCuts.printFloat(flt);
    }

    public void prntStrArr(String[] strArr) {//Prints String[] data to console
        Shortcuts sCuts = new Shortcuts();
        sCuts.printStrArr(strArr);
    }

    public String deviceOptions() { //Lists devices available to choose from
        String options = " AVAILABLE DEVICE LIST OPTIONS \n" + " These are standard devices that can be attached to\n" +
                " the smart plug: \n" + " 1-Lamp \n 2-TV \n 3-Computer \n 4-Phone Recharger \n 5-Heater \n";
        return options;
    }


    public void populateHome(SmartHome Home) { //Populates SmartHome with data entered by user
        for (int i = 0; i < Home.roomSize(); i++) { //Runs through array from 0 to max amount
            String Name = getString("Enter name for room " + (i + 1) + " :"); //Asks user the name of room and supplies room number
            int ID = (i + 1); //Assigns ID to room
            Home.addRoom(Name, ID); //Creates new room from data above
        }


        for (int i = 0; i < Home.plugSize(); i++) {//Runs through array from 0 to max amount
            prntString(Home.availableRooms());//Displays rooms for user to choose from
            String[] lst = {"Lamp", "TV", "Computer", "Phone Recharger", "Heater"}; //Array of devices
            int roomID = getInt("Enter which room plug " + (i + 1) + " is in: "); //Asks user where plug is situated
            int plugID = (i + 1); //Assigns ID to plug

            prntString(deviceOptions()); //Lists devices available to choose from
            int device = getInt("Please choose a device: "); //Asks user for device ID
            String name = lst[device - 1]; //Generates device name based off device ID. I.E. 1 = Lamp

            Home.addPlug(false, roomID, plugID, name, device); //Creates plug with both plug and device data
        }
    }

    /////MENU OPTIONS\\\\\\
    public void menu(SmartHome Home) {
        prntString("\t\t ************ MENU OPTIONS ************ \n" + //Displays Headings as well as options
                "\t\t ************ Please Select an Option ************\n" +
                "1 - House  Options\n" +
                "2 - Room   Options\n" +
                "3 - Plug   Options\n" +
                "4 - System Options\n");
        int Option = getInt("");

        switch (Option) { //Switch applies number entered by user to choose an option
            case 1 -> houseOptions(Home); //E.G if Option = 1 houseOptions(Home) will be called
            case 2 -> roomOptions(Home);//TESTED & WORKS
            case 3 -> plugOptions(Home);//TESTED & WORKS
            case 4 -> systemOptions(Home);//TESTED & WORKS
        }
    }

    public void houseOptions(SmartHome Home){
        prntString("\n\t\t ************ HOUSE LEVEL OPTIONS ************ \n"+ //Displays Headings as well as options
                "\t\t ************ Please Select an Option ************\n" +
                        "1 - Switch all plugs off\n"+
                        "2 - Switch all plugs on");

        int Option = getInt(""); //Blank variable ready for user input. Used to choose an option.

        switch (Option) {
            case 1 -> Home.plugsOff(); //Sets all plugs to False
            case 2 -> Home.plugsOn(); //Sets all plugs to True
        }

    }
    public void roomOptions(SmartHome Home){
        prntString("\n\t\t ************ ROOM LEVEL OPTIONS ************ \n"+//Displays Headings as well as options
                "\t\t ************ Please Select an Option ************\n" +
                "1 - Turn   Room Off\n" +
                "2 - Turn   Room On\n" +
                "3 - Toggle Switch\n");
        int Option = getInt("");


        switch (Option) {
            case 1:
                prntString(Home.availableRooms()); //Displays rooms
                int roomOff = getInt("Select the room: "); //Asks user to choose the room
                Home.turnRoomOff(roomOff);//Sets status of all plugs in selected room to false
                break;
            case 2:
                prntString(Home.availableRooms());//Displays rooms
                int roomOn = getInt("Select the room: "); //Asks user to choose the plug
                Home.turnRoomOn(roomOn);//Sets status of all plugs in selected room to True
                break;
            case 3:
                Home.Display();//Displays SmartHome
                int plug = getInt("Select the plug: "); //Asks user to choose the plug
                Home.toggle(plug);//Sets status of selected plug to opposite of what it currently is
                break;
        }

    }
    public void plugOptions(SmartHome Home){
        prntString("\n\n\t ************ PLUG LEVEL OPTIONS ************ \n"+//Displays Headings as well as options
                "\t\t ************ Please Select an Option ************\n" +
                "1 - Turn   Plug Off\n" +
                "2 - Turn   Plug On\n" +
                "3 - Change Device\n" +
                "4 - Move   Plug\n");
        int Option = getInt("");

        switch (Option) {
            case 1:
                int plugOn = getInt("Select the plug: ");//Asks user to choose the plug
                Home.toggleSingle(plugOn, false); //Calls ToggleSingle from SmartHome to turn on selected plug
                break;
            case 2:
                int plugOff = getInt("Select the plug: "); //Asks user to choose the plug
                Home.toggleSingle(plugOff, true); //Calls ToggleSingle from SmartHome to turn off selected plug
                break;
            case 3:
                Home.Display(); // Displays Current Home Setup
                int plug = getInt("Select the plug: "); //Asks user for the plug the device is connected to
                prntString(deviceOptions()); //Displays devices to choose from
                int device = getInt("Select device from above: "); //Asks user to choose a device from the list
                Home.changeDevice(plug, device); //Allocates device to plug
                break; //Exits
            case 4:
                plug = getInt("Select the plug: ");//Asks user to choose the plug
                int newRoom = getInt("Select the new Room: ");//Asks user to choose the new room
                Home.movePlug(plug, newRoom); //Calls movePlug from SmartHome to move selected plug to new room
                break;
        }
    }
    public void systemOptions(SmartHome Home){ //DOES NOT WORK
        prntString("\n\t\t ************ SYSTEM LEVEL OPTIONS ************ \t\n"+ //Displays Headings as well as options
                "\t\t ************ Please Select an Option ************\n" +
                "1 - Add a New Plug\n" +
                "2 - Add a New Device\n" +
                "3 - Add a New Room\n");

        int Option = getInt("Select an option: ");

        switch (Option) {
            case 1:
                prntString(Home.availableRooms());
                int room = getInt("Select the room: ");
                prntString(deviceOptions());
                int deviceID = getInt("Select the device: ");
                Home.addNewPlug(room, deviceID);
                break;
            case 2:
                Home.addNewDevice();
                break;
            case 3:
                Home.addNewRoom();
                break;

        }
    }
}

