import React from 'react';
import Header from './components/Header';
import Footer from './components/Footer';
import Vid from './components/Vid';
import {BrowserRouter as Router,Route,Routes} from 'react-router-dom'
import { Container } from 'react-bootstrap';
import HomeScreen from './screens/HomeScreen';
import ProductScreen from './screens/ProductScreen';
function App() {
  return (
    <Router>
      <div>
        <Header />
        <main className="py-5">
          <Container>
            <Routes>
              <Route path="/" element={<HomeScreen />} exact />
              <Route path='/product/:id'element={<ProductScreen/>}/>
            </Routes>
          </Container>
        </main>
        <Footer />
      </div>
    </Router>
  );
}
export default App;
