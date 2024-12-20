// App.tsx
import React from 'react';
import { QueryClient, QueryClientProvider } from 'react-query';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { ChakraProvider } from '@chakra-ui/react';
import { RecoilRoot } from 'recoil';
import Dashboard from './components/Dashboard';
import Login from './components/Login';
import PrivateRoute from './components/PrivateRoute';
import { WebSocketProvider } from './context/WebSocketContext';

const queryClient = new QueryClient();

const App: React.FC = () => {
  return (
    <RecoilRoot>
      <QueryClientProvider client={queryClient}>
        <ChakraProvider>
          <WebSocketProvider>
            <Router>
              <Routes>
                <Route path="/login" element={<Login />} />
                <Route
                  path="/"
                  element={
                    <PrivateRoute>
                      <Dashboard />
                    </PrivateRoute>
                  }
                />
              </Routes>
            </Router>
          </WebSocketProvider>
        </ChakraProvider>
      </QueryClientProvider>
    </RecoilRoot>
  );
};
export default App;

// context/WebSocketContext.tsx
import React, { createContext, useContext, useEffect, useRef } from 'react';
import { useRecoilState } from 'recoil';
import { tasksState } from '../atoms/tasks';

const WebSocketContext = createContext<WebSocket | null>(null);

export const WebSocketProvider: React.FC = ({ children }) => {
  const wsRef = useRef<WebSocket | null>(null);
  const [tasks, setTasks] = useRecoilState(tasksState);

  useEffect(() => {
    wsRef.current = new WebSocket('ws://localhost:8000/ws/' + Math.random());

    wsRef.current.onmessage = (event) => {
      const data = JSON.parse(event.data);
      if (data.type === 'task_created') {
        setTasks([...tasks, data.task]);
      }
    };
