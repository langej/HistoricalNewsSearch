import { Component, OnInit } from '@angular/core';
import {Router} from "@angular/router";
import {SearchService} from "../shared/search.service";
import {Newspaper} from "../shared/Newspaper";

@Component({
  selector: 'hs-result-list',
  templateUrl: './result-list.component.html',
  styles: []
})
export class ResultListComponent implements OnInit {

  private query: string;
  private newspapers: Newspaper[];

  //TODO: Edit so that query is still visible in searchbar

  constructor(private router: Router, private searchService: SearchService) {
    if (this.router.url !== '/search') {
      let url = this.cleanUrl();
      this.query = url;
      this.newspapers = this.searchService.getSearchResults(this.query);
    }
  }

  private cleanUrl() {
    let url = this.router.url.split('?q=')[1];
    url = url.replace(/%20/g, ' ');
    return url;
  }

  ngOnInit() {
  }
}
