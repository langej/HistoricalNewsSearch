import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Newspaper } from "./Newspaper";
import {Observable} from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class SearchService {

  private api = 'http://localhost:5000/';

  constructor(private http: HttpClient) { }

  getSearchResults(query: string): Array<Newspaper> {
    const results = Array<Newspaper>();

    this.http.get(this.api + query).subscribe( (data: any) => {
      if (data.Items !== 0) {
        Object.entries(data).forEach(([key, value]) => {
          const content = <any> value;
          const res: Newspaper = {
            id: content._id,
            source: content._source
          };
          results.push(res);
        });
      }
    });
    return results;
  }
}
