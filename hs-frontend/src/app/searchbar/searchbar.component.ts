import { Component, OnInit } from '@angular/core';
import { SearchService } from '../search.service';
import { Result } from '../Result';

@Component({
  selector: 'hs-searchbar',
  templateUrl: './searchbar.component.html',
  styleUrls: ['./searchbar.component.css']
})
export class SearchbarComponent implements OnInit {

  query = '';

  results = Array<Result>();

  constructor(private searchService: SearchService) { }

  ngOnInit() {
  }

  loadData(query: string) {
    this.results = this.searchService.getSearchResults(query);
  }

}
