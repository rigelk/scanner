import React, { Component } from 'react';
import Scanner from './Scanner';
import './App.css';
import config from './config';

const TYPE_LABELS = {
  invite: 'Invité⋅e',
  participant: 'Participant⋅e',
  volontaire: 'Volontaire',
  volontaire_referent: 'Volontaire référent⋅e',
  village: 'Village',
  so: 'Accueil et SO',
}

const EVENT_LABELS = {
  entrance: 'Entrée validée',
  scan: 'Code scanné',
  cancel: 'Scan annulé'
}

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {action: 'wait'};
  }

  startScanning() {
    this.setState({action: 'scan'});
  }

  wait() {
    this.setState({action: 'wait'});
  }

  successfulScan(registration, code) {
    this.setState({action: 'displayRegistration', registration, code});
  }

  async validateScan() {
    let form = new FormData();
    form.append('type', 'entrance');

    await fetch(config.host + '/api/' + this.state.code + '/', {
      method: 'POST',
      body: form,
    });

    this.setState({action: 'scan'});
  }

  async cancelScan() {
    let form = new FormData();
    form.append('type', 'cancel');

    await fetch(config.host + '/api/' + this.state.code + '/', {
      method: 'POST',
      body: form,
    });

    this.setState({action: 'scan'});
  }

  render() {
    switch (this.state.action) {
      case 'displayRegistration':
        let registration = this.state.registration;
        return (
          <div id="registration" className={"container registration-" + registration.type}>
            <h1 className="text-center">{`${registration.first_name} ${registration.last_name}`}</h1>
            <h3>Rôle&nbsp;: {TYPE_LABELS[registration.type]}</h3>
            <h3>#{registration.numero}</h3>
            <p><b>Genre&nbsp;:</b> {registration.gender}</p>
            <p><b>Historique&nbsp;:</b></p>
            <ul>{registration.events.map((event) => (
                <li key={event.time}>{EVENT_LABELS[event.type]} le {new Date(event.time).toLocaleString()}</li>
            ))}</ul>
            {registration.events.find(event => event.type === 'entrance') ? (
              <div className="alert alert-danger">
                Ce billet a déjà été scanné&nbsp;! Ne laissez entrer la personne
                qu'après vérification de son identité.
              </div>
            ) : ''}
            <button className="btn btn-block btn-success" onClick={this.validateScan.bind(this)}>OK</button>
            <button className="btn btn-block btn-danger" onClick={this.cancelScan.bind(this)}>Annuler</button>
          </div>
        );
      case 'scan':
        return (
          <Scanner clickBack={this.wait.bind(this)} successfulScan={this.successfulScan.bind(this)}/>
        );
      case 'wait':
      default:
        return (
          <div id="home">
            <button className="btn btn-success btn-block" onClick={this.startScanning.bind(this)}>Scanner</button>
          </div>
        )
    }
  }
}

export default App;
