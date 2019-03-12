import {Component, Input, OnInit, Sanitizer} from '@angular/core';
import {Newspaper} from "../shared/Newspaper";
import { encodeUriQuery } from '@angular/router/src/url_tree';
import { EvaluationElement } from '../shared/EvaluationElement';
import { Router } from '@angular/router';
import { SafeHtml, DomSanitizer } from '@angular/platform-browser';

@Component({
  selector: 'hs-result-element',
  templateUrl: './result-element.component.html',
  styleUrls: ['result-element.component.css']
})
export class ResultElementComponent implements OnInit {

  @Input()
  newspaper: Newspaper;

  newspaperSnippet: SafeHtml;

  @Input()
  index: number;
  relevant: boolean;
  evaluated: boolean;

  @Input()
  displayEvaluation: boolean;

  constructor(private router: Router, private sanitizer: DomSanitizer) {}

  ngOnInit() {
    const item: EvaluationElement = JSON.parse(localStorage.getItem(`evaluation-${this.index}`));
    this.evaluated = item.evaluated;
    this.relevant = item.relevant;
    this.highlightText();
  }

  navigateToDetails() {
    this.router.navigate([`/newspaper/${this.newspaper.id}`]);
  }

  evaluate(relevant: boolean) {
    const evaluationElement: EvaluationElement = JSON.parse(localStorage.getItem(`evaluation-${this.index}`));
    if (relevant) {
      evaluationElement.relevant = true;
      this.relevant = true;
    } else {
      evaluationElement.relevant = false;
      this.relevant = false;
    }
    evaluationElement.evaluated = true;
    this.evaluated = true;
    localStorage.setItem(`evaluation-${this.index}`, JSON.stringify(evaluationElement));
  }

  highlightText() {
    // let text = this.newspaper.source.Text.substring(0, 750) + ' (...)';

    let text = ''

    this.newspaper.source.Text.map(
      elem => {
        elem.map(
          elem => {
            let tmp = elem.join(' ')
            text = text.concat(tmp)
          }
        )
        text = text.concat(' ')
      }
    )

    text = text.substring(0, 1000) + ' (...)';

    let query = decodeURI(localStorage.getItem('query'));
    let queryWords = query.split(" ");

    queryWords.map( (value) => {
      text = text.replace(new RegExp(` ${value} `, 'gi'), ` <span style="background: yellow;">${value}</span> `);
    });

    this.newspaperSnippet = this.sanitizer.bypassSecurityTrustHtml(text);
  }

}
