import { Component, OnInit } from '@angular/core';
import { Router } from "@angular/router";
import {SearchService} from "../shared/search.service";

@Component({
  selector: 'hs-searchbar',
  templateUrl: './searchbar.component.html',
  styleUrls: []
})
export class SearchbarComponent implements OnInit {

  private query: string;

  constructor(private router: Router) {
  }

  ngOnInit() {
  }

  navigate() {
    this.router.navigate(["/search"], { queryParams: { q: this.query }});
  }
}
