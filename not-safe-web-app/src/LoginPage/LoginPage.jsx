import React from 'react';

import { userService } from '../_services';
import axios from 'axios';

class LoginPage extends React.Component {
    constructor(props) {
        super(props);
        userService.logout();
        this.state = {
            username: '',
            password: '',
            submitted: false,
            loading: false,
            error: '',
            similarityPercentage: 0
        };
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(e) {
        const { name, value } = e.target;
        this.setState({ [name]: value });
    }

    handleSubmit(e) {
        e.preventDefault();

        console.log("CALLED");
        
        this.setState({ submitted: true });
        const { username, password, returnUrl } = this.state;

        // console.log(password);
        

        // stop here if form is invalid
        if (!(password)) {
            return;
        }

        this.setState({ loading: true });

        axios.post(`http://127.0.0.1:5000/compute-strength`, {
            username, password
          })
          .then(response => {
            this.setState({loading: false , similarityPercentage: response.data.similarityPercentage})
        })
        .catch(error => {
            console.log(error.response)
            this.setState({ error, loading: false })
        });
    }

    render() {
        const { username, password, submitted, loading, error } = this.state;
        return (
            <div className="col-md-6 col-md-offset-3">
                <h2> <i>Not</i>SAFE </h2>
                <br></br>
                <form name="form" onSubmit={this.handleSubmit}>
                    
                    <div className={'form-group' + (submitted && !password ? ' has-error' : '')}>
                        <label htmlFor="password">Password</label>
                        <input type="text" className="form-control" name="password" value={password} onChange={this.handleChange} />
                        {submitted && !password &&
                            <div className="help-block">Password is required</div>
                        }
                    </div>
                    <div className="form-group">
                        <button className="btn btn-primary" disabled={loading}>Check</button>
                        {loading &&
                            <img src="data:image/gif;base64,R0lGODlhEAAQAPIAAP///wAAAMLCwkJCQgAAAGJiYoKCgpKSkiH/C05FVFNDQVBFMi4wAwEAAAAh/hpDcmVhdGVkIHdpdGggYWpheGxvYWQuaW5mbwAh+QQJCgAAACwAAAAAEAAQAAADMwi63P4wyklrE2MIOggZnAdOmGYJRbExwroUmcG2LmDEwnHQLVsYOd2mBzkYDAdKa+dIAAAh+QQJCgAAACwAAAAAEAAQAAADNAi63P5OjCEgG4QMu7DmikRxQlFUYDEZIGBMRVsaqHwctXXf7WEYB4Ag1xjihkMZsiUkKhIAIfkECQoAAAAsAAAAABAAEAAAAzYIujIjK8pByJDMlFYvBoVjHA70GU7xSUJhmKtwHPAKzLO9HMaoKwJZ7Rf8AYPDDzKpZBqfvwQAIfkECQoAAAAsAAAAABAAEAAAAzMIumIlK8oyhpHsnFZfhYumCYUhDAQxRIdhHBGqRoKw0R8DYlJd8z0fMDgsGo/IpHI5TAAAIfkECQoAAAAsAAAAABAAEAAAAzIIunInK0rnZBTwGPNMgQwmdsNgXGJUlIWEuR5oWUIpz8pAEAMe6TwfwyYsGo/IpFKSAAAh+QQJCgAAACwAAAAAEAAQAAADMwi6IMKQORfjdOe82p4wGccc4CEuQradylesojEMBgsUc2G7sDX3lQGBMLAJibufbSlKAAAh+QQJCgAAACwAAAAAEAAQAAADMgi63P7wCRHZnFVdmgHu2nFwlWCI3WGc3TSWhUFGxTAUkGCbtgENBMJAEJsxgMLWzpEAACH5BAkKAAAALAAAAAAQABAAAAMyCLrc/jDKSatlQtScKdceCAjDII7HcQ4EMTCpyrCuUBjCYRgHVtqlAiB1YhiCnlsRkAAAOwAAAAAAAAAAAA==" />
                        }
                    </div>

                    {this.state.similarityPercentage > 0 && (this.state.similarityPercentage > 70 ? <div className={'alert alert-danger'}>{`Password is ${this.state.similarityPercentage}% similar to one of the AI generated passwords`}</div>:<div className={'alert alert-success'}>{`Password is ${this.state.similarityPercentage}% similar to one of the AI generated passwords`}</div> )}
                    

                    {this.state.similarityPercentage > 0 && (this.state.similarityPercentage > 70 ? <img src="failure.gif" align="middle" height="256" width="256"></img>:<img src="success.gif" align="middle"  height="256" width="256"></img> )}



                </form>
            </div>
        );
    }
}

export { LoginPage }; 