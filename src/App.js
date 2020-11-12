import React from 'react';
import { Route, Redirect } from 'react-router-dom';
import { router } from './router'

const App = () => <div>
  {
    router.map( (props) =>
      props.redirect
      ? <Redirect from={props.pathname} to={props.to} />
      : <Route path={props.pathname} component={props.components} />
    )
  }
</div>

export default App;
