import { Component, OnInit } from '@angular/core';
import {ActivatedRoute, Router} from "@angular/router";
import {SearchService} from "../shared/search.service";
import {Newspaper} from "../shared/Newspaper";

@Component({
  selector: 'hs-result-list',
  templateUrl: './result-list.component.html',
  styleUrls: ['./result-list.component.css'],
  providers: [SearchService]
})
export class ResultListComponent implements OnInit {

  private newspapers: Newspaper[];

  // TODO: Edit so that query is still visible in searchbar

  constructor(private router: Router, private searchService: SearchService) {
    // if (this.router.url !== '/search') {
    //   const url = this.cleanUrl();
    //   // this.newspapers = this.searchService.getSearchResults(url);
    // }

    this.router.routeReuseStrategy.shouldReuseRoute = () => false;
  }

  ngOnInit() {
    this.newspapers = new Array<Newspaper>();
    if (this.router.url !== '/search') {
      const url = this.cleanUrl();
      this.searchService.getSearchResults(url).then( (results) => {
        results.map( (data) => {
          this.newspapers.push(data);
        });
        console.log(this.newspapers);
      });
    }
  }

  private cleanUrl() {
    let url = this.router.url.split('?q=')[1];
    url = url.replace(/%20/g, ' ');
    return url;
  }
}
