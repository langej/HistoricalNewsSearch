import { Injectable } from '@angular/core';
import Axios from 'axios';
import { EvaluationElement } from './EvaluationElement';

@Injectable({
  providedIn: 'root'
})
export class EvaluationService {

  private api = 'http://localhost:5000/';

  constructor() { }

  postEvaluation(payload: EvaluationElement[]) {
    const data = {
      date: new Date().toISOString(),
      query: localStorage.getItem('query'),
      documents: payload
    };
    Axios({
      method: 'post',
      url: this.api + 'evaluation',
      data: data,
      headers: {
        'Access-Control-Allow-Origin': '*',
        'Content-Type': 'application/json',
        'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS, HEAD',
        "Access-Control-Allow-Headers": "Access-Control-*, Origin, X-Requested-With, Content-Type, Accept"
      }
    }).then(
      // (response) => console.log(response)
    ).catch(
      // (err) => console.log(err)
    );
  }
  //     this.api + 'evaluation', payload,
  //     {
  //       headers: {
  //         'Access-Control-Allow-Origin': '*',
  //         'Content-Type': 'application/json' 
  //       }
  //     }).then().catch();
  // }}
}
