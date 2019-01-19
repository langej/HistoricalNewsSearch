import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Newspaper } from "./Newspaper";
import {Observable} from "rxjs";
import axios from 'axios';
import { EvaluationElement } from './EvaluationElement';

@Injectable({
  providedIn: 'root'
})
export class SearchService {

  private api = 'http://localhost:5000/';

  constructor(private http: HttpClient) { }

  async getSearchResults(query: string) {
    const oldQuery = localStorage.getItem('query');
    if (oldQuery !== query) {
      localStorage.clear();
    }
    localStorage.setItem('query', query);
    const response = await axios.get(this.api + query);
    const newspapers = new Array<Newspaper>();
    if (typeof(response.data) !== 'string') {
      Object.entries(response.data).forEach(([key, value], index) => {
        const content = <any> value;
        const res: Newspaper = {
          id: content._id,
          source: content._source
        };
        newspapers.push(res);
        localStorage.setItem(res.id, JSON.stringify(res.source));
        if (oldQuery !== query) {
          const evaluationElement: EvaluationElement = {
            index: index,
            id: res.id,
            relevant: false,
            evaluated: false
          };
          localStorage.setItem(`evaluation-${index}`, JSON.stringify(evaluationElement));
        }
      });
    }
    return newspapers;
  }
}
