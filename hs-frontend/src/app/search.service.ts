import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Result } from './Result';

@Injectable({
  providedIn: 'root'
})
export class SearchService {

  constructor(private http: HttpClient) { }

  getSearchResults(query: string): Array<Result> {
    const results = Array<Result>();

    this.http.get('http://localhost:5000/' + query).subscribe( (data: any) => {
      if (data.Items !== 0) {
        Object.entries(data).forEach(([key, value]) => {
          const res: Result = {
            id: value._id,
            source: value._source
          };
          results.push(res);
        });
      }
    });
    return results;
  }
}
