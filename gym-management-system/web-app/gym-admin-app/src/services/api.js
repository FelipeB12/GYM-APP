import axios from 'axios';
import firebase from '../firebase';

const API_URL = process.env.REACT_APP_API_URL;

const api = axios.create({
  baseURL: API_URL,
});

api.interceptors.request.use(async (config) => {
  const user = firebase.auth().currentUser;
  if (user) {
    const token = await user.getIdToken();
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export const fetchAttendanceData = () => api.get('/attendance/');
export const fetchClients = () => api.get('/clients/');
export const fetchAppointments = () => api.get('/appointments/');
export const createAppointment = (data) => api.post('/appointments/', data);

export default api;