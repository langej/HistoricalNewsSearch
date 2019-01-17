import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Newspaper } from "./Newspaper";
import {Observable} from "rxjs";
import axios from 'axios';

@Injectable({
  providedIn: 'root'
})
export class SearchService {

  private api = 'http://localhost:5000/';

  constructor(private http: HttpClient) { }

  async getSearchResults(query: string) {
    localStorage.clear();
    const response = await axios.get(this.api + query);
    const newspapers = new Array<Newspaper>();
    if (typeof(response.data) !== 'string') {
      Object.entries(response.data).forEach(([key, value]) => {
        const content = <any> value;
        const res: Newspaper = {
          id: content._id,
          source: content._source
        };
        newspapers.push(res);
        localStorage.setItem(res.id, JSON.stringify(res.source));
      });
    }
    return newspapers;
  }
}
