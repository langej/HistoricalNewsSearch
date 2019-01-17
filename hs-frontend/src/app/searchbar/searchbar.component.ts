import { Component, OnInit } from '@angular/core';
import {ActivatedRoute, Router} from "@angular/router";
import {SearchService} from "../shared/search.service";

@Component({
  selector: 'hs-searchbar',
  templateUrl: './searchbar.component.html',
  styleUrls: ['./searchbar.component.css']
})
export class SearchbarComponent implements OnInit {

  query: string;

  constructor(private router: Router, private activeRoute: ActivatedRoute) {
    this.activeRoute.queryParams.subscribe(params => {
      this.query = params["q"];
    });
  }

  ngOnInit() {
  }

  navigate() {
    this.router.navigate(["/search"], { queryParams: { q: this.query }});
  }
}
