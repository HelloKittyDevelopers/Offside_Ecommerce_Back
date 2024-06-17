import React from 'react'
import products from '../products'
import {Row, Col} from 'react-bootstrap'
import Product from '../components/Product'
import Vid from '../components/Vid'
function HomeScreen() {
    return (
        <div>
            <Vid/>
            <h1>Latest Products</h1>
            <Row>
                {products.map(product => (
                    <Col key={product._id} sm={12} md={6} Lg={4} xL={3}>

                        <Product product={product} />
                    </Col>
                ))}
            </Row>
        </div>
    )
    
}
export default HomeScreen