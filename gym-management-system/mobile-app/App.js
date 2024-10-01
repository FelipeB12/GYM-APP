// Import necessary modules and components from React and React Navigation
import React from 'react';  // Importing React for creating the App component.
import { NavigationContainer } from '@react-navigation/native';  // The root component for managing navigation.
import { createStackNavigator } from '@react-navigation/stack';  // Stack navigation creates a stack-based navigation flow.

// Importing screen components to be used in navigation
import LoginScreen from './src/screens/LoginScreen';  // Login screen component, the initial screen for the app.
import HomeScreen from './src/screens/HomeScreen';  // Home screen component, likely the main dashboard after login.
import MeasurementsScreen from './src/screens/MeasurementsScreen';  // Screen for viewing and managing user measurements.
import PersonalRecordsScreen from './src/screens/PersonalRecordsScreen';  // Screen to track personal fitness records.
import RoutineScreen from './src/screens/RoutineScreen';  // Screen where users can view or edit workout routines.
import AIChatScreen from './src/screens/AIChatScreen';  // Screen where users can interact with an AI-powered chat system.
import AppointmentScreen from './src/screens/AppointmentScreen';  // Screen for scheduling or managing appointments.


// Initialize the stack navigator
const Stack = createStackNavigator();  // Creating a stack navigator instance for navigation between screens.


// Define the main App component
const App = () => {
  return (
    <NavigationContainer>  {/* The root navigation container that manages the navigation state */}
      <Stack.Navigator initialRouteName="Login">  {/* Stack.Navigator defines the navigation stack. 'initialRouteName' specifies the first screen to show. */}
        {/* Stack.Screen defines each screen in the app with a name and its corresponding component */}
        <Stack.Screen name="Login" component={LoginScreen} />  {/* The login screen is displayed first as it's set as the initial route. */}
        <Stack.Screen name="Home" component={HomeScreen} />  {/* The home screen, likely after a user logs in. */}
        <Stack.Screen name="Measurements" component={MeasurementsScreen} />  {/* Screen to display user measurements. */}
        <Stack.Screen name="PersonalRecords" component={PersonalRecordsScreen} />  {/* Screen for tracking personal fitness records. */}
        <Stack.Screen name="Routine" component={RoutineScreen} />  {/* Screen for viewing and editing workout routines. */}
        <Stack.Screen name="AIChat" component={AIChatScreen} />  {/* Screen with an AI-powered chat feature for training advice. */}
        <Stack.Screen name="Appointment" component={AppointmentScreen} />  {/* Screen for scheduling or viewing appointments. */}
      </Stack.Navigator>  {/* End of the Stack.Navigator, which manages the screen transitions. */}
    </NavigationContainer>  {/* End of the NavigationContainer that wraps the entire navigation system. */}
  );
};

// Export the App component as the default export
export default App;  // Exports the App component to be used as the root component in the project.
