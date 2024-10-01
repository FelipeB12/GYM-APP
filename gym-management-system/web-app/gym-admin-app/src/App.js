import React from 'react';
import { BrowserRouter as Router, Route, Switch, Redirect } from 'react-router-dom';
import { ThemeProvider, createTheme } from '@material-ui/core/styles';
import CssBaseline from '@material-ui/core/CssBaseline';
import LoginPage from './pages/LoginPage';
import DashboardPage from './pages/DashboardPage';
import ClientsPage from './pages/ClientsPage';
import AppointmentsPage from './pages/AppointmentsPage';
import PrivateRoute from './components/PrivateRoute';

const theme = createTheme({
  palette: {
    type: 'light',
    primary: {
      main: '#1976d2',
    },
    secondary: {
      main: '#dc004e',
    },
  },
});

function App() {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Router>
        <Switch>
          <Route exact path="/login" component={LoginPage} />
          <PrivateRoute exact path="/dashboard" component={DashboardPage} />
          <PrivateRoute exact path="/clients" component={ClientsPage} />
          <PrivateRoute exact path="/appointments" component={AppointmentsPage} />
          <Redirect from="/" to="/dashboard" />
        </Switch>
      </Router>
    </ThemeProvider>
  );
}

export default App;