package IOT_System;

public class Dashboard {

    public static void main(String[] args) {
        //BUILD SMARTHOME & CONSOLE HELPER OBJECTS
        ConsoleOutput console = new ConsoleOutput();
        console.prntString("\t\t\t  ************ WELCOME TO ALIKOTI SMARTHOME ************\n"+
                          "\t\t ************ PLEASE USE NUMBER INPUT FOR ALL DATA ************\n"+
                          "\t\t\t\t\t   ************ THANK YOU ************\n");

        int rooms = console.getInt("How many rooms are there: ");//Asks user the amount of rooms
        int plugs = console.getInt("How many plugs are there: ");//Asks user the amount of plugs
        SmartHome Home = new SmartHome(rooms, plugs);//Creates SmartHome object consisting of room and plug size data

        console.populateHome(Home);//Populates SmartHome based off the sizes entered by user


    //POPULATE SMARTHOME
        while(true){
            Home.Display();//Displays Dashboard consisting of Devices, Rooms and Plug
            console.menu(Home);//Displays Menu, including sub-menus for house, room, plug and system options
        }
    }
}
