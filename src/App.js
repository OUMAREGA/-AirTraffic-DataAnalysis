import React from 'react';
import { Route, Redirect } from 'react-router-dom';
import { router } from './router'
import Header from './components/Header';
import Footer from './components/Footer';

const App = () => <main>
  <Header />
  {
    <div id="page-container">
    { router.map( (props) =>
      props.redirect
      ? <Redirect from={props.pathname} to={props.to} />
      : <Route path={props.pathname} component={props.components} />
    )}
    </div>
  }
  <Footer />
</main>

export default App;
