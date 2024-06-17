import React from 'react'
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
function Header() {
    return (
      <header>
        <br />
        <Navbar bg="light" data-bs-theme="light" collapseOnSelect>
          <Container>
            <Navbar.Brand href="#home">Offside</Navbar.Brand>
            <Nav className="me-auto">
              <Nav.Link href="#retros">Retro Kits</Nav.Link>
              <Nav.Link href="#FAQ">FAQ</Nav.Link>
            </Nav>
            <Nav className="ml-auto">
              <Nav.Link href="#Login"><i className='fas fa-user'></i> Login</Nav.Link>
              <Nav.Link href="#Cart"><i className='fas fa-shopping-cart'></i> Cart</Nav.Link>
            </Nav>
          </Container>
        </Navbar>
      </header>
    );
  }
  
  export default Header;